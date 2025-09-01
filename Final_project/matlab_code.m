function open3d_matlab_example()
    % Create test data file
    f = fopen('tof_radar.xyz', 'w');

    % Generate prism vertices
    for x = 0:9
        fprintf(f, '%d 0 0\n', x);  % p1: x,0,0
        fprintf(f, '%d 0 1\n', x);  % p2: x,0,1
        fprintf(f, '%d 1 1\n', x);  % p3: x,1,1
        fprintf(f, '%d 1 0\n', x);  % p4: x,1,0
    end
    fclose(f);

    % Read the point cloud data - CORRECTED LINE
    fprintf("Read in the prism point cloud data (pcd)\n");
    pcd = readmatrix('demofile2dx.xyz', 'FileType', 'text');

    % Rest of the code remains the same...
    disp("The PCD array:");
    disp(pcd);

    fprintf("Lets visualize the PCD:\n");
    figure;
    scatter3(pcd(:,1), pcd(:,2), pcd(:,3), 'filled');
    title('Point Cloud Visualization');
    xlabel('X');
    ylabel('Y');
    zlabel('Z');
    grid on;
    axis equal;

    lines = [];
    for x = 1:4:37
        lines = [lines; x, x+1];
        lines = [lines; x+1, x+2];
        lines = [lines; x+2, x+3];
        lines = [lines; x+3, x];
    end

    for x = 1:4:33
        lines = [lines; x, x+4];
        lines = [lines; x+1, x+5];
        lines = [lines; x+2, x+6];
        lines = [lines; x+3, x+7];
    end

    figure;
    hold on;
    scatter3(pcd(:,1), pcd(:,2), pcd(:,3), 'filled');
    for i = 1:size(lines, 1)
        plot3(pcd(lines(i,:), 1), pcd(lines(i,:), 2), pcd(lines(i,:), 3), 'b-');
    end
    title('Point Cloud with Line Connections');
    xlabel('X');
    ylabel('Y');
    zlabel('Z');
    grid on;
    axis equal;
    hold off;
end