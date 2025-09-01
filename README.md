# Microprocesser-Systems-Project-
3D Indoor Mapping System using ToF Sensor and Microcontroller

This project implements a cost-effective 3D indoor mapping system using a **Time-of-Flight (ToF) sensor (VL53L1X)**, a **Texas Instruments MSP432E401Y microcontroller**, and a **28BYJ-48 stepper motor**.  

---

## 🚀 Project Overview
The system scans an indoor environment by rotating a ToF sensor mounted on a stepper motor, capturing distance data, and transmitting it to a PC. Python scripts process the data and generate a **3D point cloud visualization** of the scanned area.

- **Hardware Used**  
  - TI MSP432E401Y (ARM Cortex-M4 @ 120 MHz, 3.3V logic)  
  - VL53L1X Time-of-Flight sensor (max 4m range, I2C communication)  
  - 28BYJ-48 stepper motor with ULN2003 driver  
  - Custom wiring and 3D-printed sensor mount  

- **Software Used**  
  - **C (Keil uVision)** for microcontroller firmware  
  - **Python 3.11.9** for PC data handling and visualization  
    - [PySerial](https://pypi.org/project/pyserial/) for UART communication  
    - [Open3D](http://www.open3d.org/) for 3D visualization   

---

## 📡 System Communication
- **I2C**: VL53L1X → MSP432E401Y (distance data at 167 kbps)  
- **UART**: MSP432E401Y → PC (115200 baud)  
- **Visualization**: Python + Open3D to render `.xyz` point cloud files  

---

## 📊 Workflow
1. ToF sensor collects distance measurements every 11.25° (32 points per rotation).  
2. Stepper motor rotates the sensor for a full 360° scan.  
3. Data sent via I2C to microcontroller → relayed to PC over UART.  
4. Python processes raw data into (x, y, z) coordinates.  
5. Open3D generates a 3D visualization of the scanned room.  

---

## 📸 Results
- **Generated Point Cloud Visualization**
 
  Preview of 3D visualization 
  <img width="875" height="561" alt="Screenshot 2025-03-27 213340" src="https://github.com/user-attachments/assets/215b2f6e-57fe-4690-adb1-d4b82d0fe1bc" />


  3D Data Visualization 
  <img width="902" height="585" alt="Screenshot 2025-03-27 213728" src="https://github.com/user-attachments/assets/f07ac938-117d-46d0-95d4-42eaeca81873" />


  Live image we imitated 
  ![IMG_4223 (2)](https://github.com/user-attachments/assets/77cf393b-ed12-4626-a474-41dfbf0646e8)


---


The setup for running this project and all other detailed information is provided in the report: [Final Report (PDF)](_2DX3_Final_Report.pdf)



