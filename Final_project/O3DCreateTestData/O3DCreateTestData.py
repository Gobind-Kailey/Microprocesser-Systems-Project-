import serial
import numpy as np
import open3d as o3d
import math

# Define the angle sequence (in degrees) we are traveling clockwise 

angles_deg = [
    180.00, 168.75, 157.50, 146.25, 135.00, 123.75, 112.50, 101.25,
    90.00, 78.75, 67.50, 56.25, 45.00, 33.75, 22.50, 11.25,
    0.00, -11.25, -22.50, -33.75, -45.00, -56.25, -67.50, -78.75,
    -90.00, -101.25, -112.50, -123.75, -135.00, -146.25, -157.50, -168.75
]

z_displacement_values = [0, 1000,2000,3000,4000,5000,6000,7000,8000, 9000, 10000, 11000 ,12000, 13000, 14000,15000]
j = 0 # this is an index value for Z_values 
k = 0  # this is the index for angles 
a= 1
# Serial setup
s = serial.Serial('COM3', 115200, timeout=10)
print("Opening: " + s.name)
s.reset_output_buffer()
s.reset_input_buffer()
x
layers = 96
processed = 0

# Open file for writing
with open("tof_radar.xyz", "w") as f: 
    # Signal MCU to start
    input("press enter")
    s.write('s'.encode())

    
    
    
    while (processed != layers):

        
        try:
            print("current spot" , processed%32)
            raw_data = s.readline().decode().strip()  # E.g., "0, 16, 41720, 0, 1"
            print(f"Raw data (string): {raw_data}")  # Debug output

# Split into parts using commas
            parts = raw_data.split(',')  # Now a list: ["0", " 16", " 41720", " 0", " 1"]
            print(f"Split parts: {parts}")  # Debug output

# Extract distance (2nd value), remove spaces, convert to int
            distance = int(parts[1].strip())  # " 16" → "16" → 16
            print(f"Distance extracted: {distance}")  # Debug output

            # is there a need for this line here? 
            # if len(parts) >= 2:
            #     distance = int(parts[1].strip())  # Get 2nd value as distance
            # else:
            #     print(f"Invalid data format: {raw_data}")
            #     continue
            
            # Convert to Cartesian coordinates


            angle_rad = math.radians(angles_deg[k])
            x = math.cos(angle_rad) * distance
            y = math.sin(angle_rad) * distance
            z = z_displacement_values[j]
            processed += 1; 

            # if a != 0:
            if (a %(len(angles_deg))) ==0 : 
                j += 1 # z value 
                k= -1 #angle 
            a+=1    
            k +=1 

            print(f"z value: {z}")
            
            
            # Write to file
            f.write(f"{x:.2f} {y:.2f} {z}\n")
            print(f"Processed: Angle={angles_deg[k]}°, Distance={distance} → ({x:.2f}, {y:.2f}, {z})")
        except (ValueError, IndexError) as e:
            print(f"Error processing line: {e}")
            continue

# Read and visualize point cloud
print("\nReading point cloud...")
pcd = o3d.io.read_point_cloud("tof_radar.xyz", format="xyz")
if not pcd.points:
    print("Warning: Point cloud is empty! Check output file.")
else:
    print("Point cloud array:")
    print(np.asarray(pcd.points))
    o3d.visualization.draw_geometries([pcd], window_name="Radar Scan")

   #Give each vertex a unique number
    yz_slice_vertex = []
    for x in range(0,96):
        yz_slice_vertex.append([x])

    #Define coordinates to connect lines in each yz slice        
    lines = []  
    # Connect lines within each yz slice

    # # The code below may work (test)
    # for x in range(0, 96, 32):
    #     for i in range(31):  # Loop through 0 to 30
    #         lines.append([yz_slice_vertex[x + i], yz_slice_vertex[x + i + 1]])
    #     lines.append([yz_slice_vertex[x + 31], yz_slice_vertex[x]])  # Closing the loop

    # # Connect lines between corresponding points in adjacent yz slices
    # for x in range(0,96, 32):
    #     for i in range(32):  # Loop through 0 to 31
    #         lines.append([yz_slice_vertex[i], yz_slice_vertex[i + 32]])

    # lines = []  
    for x in range(0,96,32):
        lines.append([yz_slice_vertex[x + 0], yz_slice_vertex[x + 1]])
        lines.append([yz_slice_vertex[x + 1], yz_slice_vertex[x + 2]])
        lines.append([yz_slice_vertex[x + 2], yz_slice_vertex[x + 3]])
        lines.append([yz_slice_vertex[x + 3], yz_slice_vertex[x + 4]])
        lines.append([yz_slice_vertex[x + 4], yz_slice_vertex[x + 5]])
        lines.append([yz_slice_vertex[x + 5], yz_slice_vertex[x + 6]])
        lines.append([yz_slice_vertex[x + 6], yz_slice_vertex[x + 7]])
        lines.append([yz_slice_vertex[x + 7], yz_slice_vertex[x + 8]])
        lines.append([yz_slice_vertex[x + 8], yz_slice_vertex[x + 9]])
        lines.append([yz_slice_vertex[x + 9], yz_slice_vertex[x + 10]])
        lines.append([yz_slice_vertex[x + 10], yz_slice_vertex[x + 11]])
        lines.append([yz_slice_vertex[x + 11], yz_slice_vertex[x + 12]])
        lines.append([yz_slice_vertex[x + 12], yz_slice_vertex[x + 13]])
        lines.append([yz_slice_vertex[x + 13], yz_slice_vertex[x + 14]])
        lines.append([yz_slice_vertex[x + 14], yz_slice_vertex[x + 15]])
        lines.append([yz_slice_vertex[x + 15], yz_slice_vertex[x + 16]])
        lines.append([yz_slice_vertex[x + 16], yz_slice_vertex[x + 17]])
        lines.append([yz_slice_vertex[x + 17], yz_slice_vertex[x + 18]])
        lines.append([yz_slice_vertex[x + 18], yz_slice_vertex[x + 19]])
        lines.append([yz_slice_vertex[x + 19], yz_slice_vertex[x + 20]])
        lines.append([yz_slice_vertex[x + 20], yz_slice_vertex[x + 21]])
        lines.append([yz_slice_vertex[x + 21], yz_slice_vertex[x + 22]])
        lines.append([yz_slice_vertex[x + 22], yz_slice_vertex[x + 23]])
        lines.append([yz_slice_vertex[x + 23], yz_slice_vertex[x + 24]])
        lines.append([yz_slice_vertex[x + 24], yz_slice_vertex[x + 25]])
        lines.append([yz_slice_vertex[x + 25], yz_slice_vertex[x + 26]])
        lines.append([yz_slice_vertex[x + 26], yz_slice_vertex[x + 27]])
        lines.append([yz_slice_vertex[x + 27], yz_slice_vertex[x + 28]])
        lines.append([yz_slice_vertex[x + 28], yz_slice_vertex[x + 29]])
        lines.append([yz_slice_vertex[x + 29], yz_slice_vertex[x + 30]])
        lines.append([yz_slice_vertex[x + 30], yz_slice_vertex[x + 31]])
        lines.append([yz_slice_vertex[x+ 31], yz_slice_vertex[x]])
        # lines.append([yz_slice_vertex[x+8], yz_slice_vertex[x]])



    #Define coordinates to connect lines between current and next yz slice        
    for x in range(0, 63 ,32):
        lines.append([yz_slice_vertex[x + 0], yz_slice_vertex[x + 32]])
        lines.append([yz_slice_vertex[x + 1], yz_slice_vertex[x + 33]])
        lines.append([yz_slice_vertex[x + 2], yz_slice_vertex[x + 34]])
        lines.append([yz_slice_vertex[x + 3], yz_slice_vertex[x + 35]])
        lines.append([yz_slice_vertex[x + 4], yz_slice_vertex[x + 36]])
        lines.append([yz_slice_vertex[x + 5], yz_slice_vertex[x + 37]])
        lines.append([yz_slice_vertex[x + 6], yz_slice_vertex[x + 38]])
        lines.append([yz_slice_vertex[x + 7], yz_slice_vertex[x + 39]])
        lines.append([yz_slice_vertex[x + 8], yz_slice_vertex[x + 40]])
        lines.append([yz_slice_vertex[x + 9], yz_slice_vertex[x + 41]])
        lines.append([yz_slice_vertex[x + 10], yz_slice_vertex[x + 42]])
        lines.append([yz_slice_vertex[x + 11], yz_slice_vertex[x + 43]])
        lines.append([yz_slice_vertex[x + 12], yz_slice_vertex[x + 44]])
        lines.append([yz_slice_vertex[x + 13], yz_slice_vertex[x + 45]])
        lines.append([yz_slice_vertex[x + 14], yz_slice_vertex[x + 46]])
        lines.append([yz_slice_vertex[x + 15], yz_slice_vertex[x + 47]])
        lines.append([yz_slice_vertex[x + 16], yz_slice_vertex[x + 48]])
        lines.append([yz_slice_vertex[x + 17], yz_slice_vertex[x + 49]])
        lines.append([yz_slice_vertex[x + 18], yz_slice_vertex[x + 50]])
        lines.append([yz_slice_vertex[x + 19], yz_slice_vertex[x + 51]])
        lines.append([yz_slice_vertex[x + 20], yz_slice_vertex[x + 52]])
        lines.append([yz_slice_vertex[x + 21], yz_slice_vertex[x + 53]])
        lines.append([yz_slice_vertex[x + 22], yz_slice_vertex[x + 54]])
        lines.append([yz_slice_vertex[x + 23], yz_slice_vertex[x + 55]])
        lines.append([yz_slice_vertex[x + 24], yz_slice_vertex[x + 56]])
        lines.append([yz_slice_vertex[x + 25], yz_slice_vertex[x + 57]])
        lines.append([yz_slice_vertex[x + 26], yz_slice_vertex[x + 58]])
        lines.append([yz_slice_vertex[x + 27], yz_slice_vertex[x + 59]])
        lines.append([yz_slice_vertex[x + 28], yz_slice_vertex[x + 60]])
        lines.append([yz_slice_vertex[x + 29], yz_slice_vertex[x + 61]])
        lines.append([yz_slice_vertex[x + 30], yz_slice_vertex[x + 62]])
        lines.append([yz_slice_vertex[x + 31], yz_slice_vertex[x + 63]])
    #This line maps the lines to the 3d coordinate vertices
    line_set = o3d.geometry.LineSet(points=o3d.utility.Vector3dVector(np.asarray(pcd.points)),lines=o3d.utility.Vector2iVector(lines))

    #Lets see what our point cloud data with lines looks like graphically       
    o3d.visualization.draw_geometries([line_set])
                                    
    

s.close()
print("Done.")


