import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
import serial
import pandas as pd
# import time
import os

error1 = np.array([12.49-9.8, -0.17, -1.45])  # Done
error2 = np.array([15.4-9.8, 1.82, 0.55])  # Done
error3 = np.array([9.78-9.8, -0.35, -1.05])  # Done
error4 = np.array([9.97-9.8, -0.14, -0.88])  # Done
error5 = np.array([10.45-9.8, -0.26, -2.02])  # Done

# error1 = np.array([0,0,0])
# error2 = np.array([0,0,0])
# error3 = np.array([0,0,0])
# error4 = np.array([0,0,0])
# error5 = np.array([0,0,0])

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
Angle1 = ax.text(0, 4, 1, "", fontsize=10, ha='left', va='center')
Angle2 = ax.text(0, 4, 3, "", fontsize=10, ha='left', va='center')
Angle3 = ax.text(0, 4, 5, "", fontsize=10, ha='left', va='center')
Angle4 = ax.text(0, 4, 7, "", fontsize=10, ha='left', va='center')
Angle5 = ax.text(0, 4, 9, "", fontsize=10, ha='left', va='center')

pos1 = [0, 0, 0]
dir1 = [0, 0, 0]
dir2 = [0, 0, 0]
dir3 = [0, 0, 0]
dir4 = [0, 0, 0]
dir5 = [0, 0, 0]

length_trunk = [2, 2, 2, 2, 2]
trunk_plt1 = ax.plot3D([], [], [], c=(0, 1, 1), linewidth=3)[0]
trunk_plt2 = ax.plot3D([], [], [], c=(0, 1, 0.8), linewidth=3)[0]
trunk_plt3 = ax.plot3D([], [], [], c=(0, 1, 0.6), linewidth=3)[0]
trunk_plt4 = ax.plot3D([], [], [], c=(0, 1, 0.4), linewidth=3)[0]
trunk_plt5 = ax.plot3D([], [], [], c=(0, 1, 0.2), linewidth=3)[0]
line_plt = ax.plot3D([], [], [], c='k', linestyle='-.', linewidth=0.7)[0]

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(-5, 5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ser = serial.Serial('COM5', 115200)
ser.flushInput()

row_list = []
column_names = []

# Define column names
for i in range(5):
    column_names.append("Angle" + str(i + 1))
for i in range(5):
    column_names.append("X" + str(i + 1))
    column_names.append("Y" + str(i + 1))
    column_names.append("Z" + str(i + 1))
# start_time = time.time()
# time_limit = 60*int(input("Insert time (minutes): "))


def move_arrow(root, direction1,
               # direction2, direction3, direction4, direction5,
               trunk_plt1,
               # trunk_plt2, trunk_plt3, trunk_plt4, trunk_plt5,
               length_trunk,
               ):
    # Converting directional inputs into arrays
    root = np.asarray(root)
    direction1 = np.asarray(direction1)
    # direction2 = np.asarray(direction2)
    # direction3 = np.asarray(direction3)
    # direction4 = np.asarray(direction4)
    # direction5 = np.asarray(direction5)

    # Normalizing
    direction1 = direction1 / np.linalg.norm(direction1)
    # direction2 = direction2 / np.linalg.norm(direction2)
    # direction3 = direction3 / np.linalg.norm(direction3)
    # direction4 = direction4 / np.linalg.norm(direction4)
    # direction5 = direction5 / np.linalg.norm(direction5)

    # Shifting vectors
    shift1 = direction1 * length_trunk[0]
    end1 = root + shift1
    # shift2 = direction2 * length_trunk[1]
    # end2 = end1 + shift2
    # shift3 = direction3 * length_trunk[2]
    # end3 = end2 + shift3
    # shift4 = direction4 * length_trunk[3]
    # end4 = end3 + shift4
    # shift5 = direction5 * length_trunk[4]
    # end5 = end4 + shift5

    axis = np.array([1, 0, 0])
    ang1 = round(np.rad2deg(np.arccos(np.clip(np.dot(direction1, axis), -1.0, 1.0))), 2)
    # ang2 = round(np.rad2deg(np.arccos(np.clip(np.dot(direction2, direction1), -1.0, 1.0))), 2)
    # ang3 = round(np.rad2deg(np.arccos(np.clip(np.dot(direction3, direction2), -1.0, 1.0))), 2)
    # ang4 = round(np.rad2deg(np.arccos(np.clip(np.dot(direction4, direction3), -1.0, 1.0))), 2)
    # ang5 = round(np.rad2deg(np.arccos(np.clip(np.dot(direction5, direction4), -1.0, 1.0))), 2)

    # print("Root angle: ", ang1,
    #       ",Ang 1/2:", ang2,
    #       ",Ang 2/3:", ang3,
    #       ",Ang 3/4:", ang4,
    #       ",Ang 4/5:", ang5
    #       )

    # ang_row = [ang1]

    ang_row = [
        ang1,
        # ang2, ang3, ang4, ang5,
        direction1[0],direction1[1],direction1[2],
        # direction2[0],direction2[1],direction2[2],
        # direction3[0],direction3[1],direction3[2],
        # direction4[0],direction4[1],direction4[2],
        # direction5[0],direction5[1],direction5[2]
    ]
    row_list.append(ang_row)

    trunk_plt1.set_data([root[0], end1[0]], [root[1], end1[1]])  # Set data
    trunk_plt1.set_3d_properties([root[2], end1[2]])  # Set properties
    # trunk_plt2.set_data([end1[0], end2[0]], [end1[1], end2[1]])
    # trunk_plt2.set_3d_properties([end1[2], end2[2]])
    # trunk_plt3.set_data([end2[0], end3[0]], [end2[1], end3[1]])
    # trunk_plt3.set_3d_properties([end2[2], end3[2]])
    # trunk_plt4.set_data([end3[0], end4[0]], [end3[1], end4[1]])
    # trunk_plt4.set_3d_properties([end3[2], end4[2]])
    # trunk_plt5.set_data([end4[0], end5[0]], [end4[1], end5[1]])
    # trunk_plt5.set_3d_properties([end4[2], end5[2]])
    #
    # line_plt.set_data([root[0], end5[0]], [root[1], end5[1]])
    # line_plt.set_3d_properties([root[2], end5[2]])

    Angle1.set_text("")
    Angle1.set_text("Z/1: {:.2f}".format(ang1))
    # # Angle1.set_position((end1[0] + 2, end1[1]))
    # Angle2.set_text("")
    # Angle2.set_text("1/2: {:.2f}".format(ang2))
    # # Angle2.set_position((end2[0] + 2, end2[1]))
    # Angle3.set_text("")
    # Angle3.set_text("2/3: {:.2f}".format(ang3))
    # # Angle3.set_position((end3[0] + 2, end3[1]))
    # Angle4.set_text("")
    # Angle4.set_text("3/4: {:.2f}".format(ang4))
    # # Angle4.set_position((end4[0] + 2, end4[1]))
    # Angle5.set_text("")
    # Angle5.set_text("4/5: {:.2f}".format(ang5))
    # # Angle5.set_position((end5[0] + 2, end5[1]))


def export():
    df = pd.DataFrame(row_list)
    print(df)
    # if time_limit > 60 * 5:
    #     filename = f"Test_{str(count)}_{str(int(time_limit/60))}min_{str(start_time)}.xlsx"
    #     df.to_excel(filename, header=column_names)
    # if time_limit <= 60 * 5:
    #     filename = f"Test_{str(count)}_{str(int(time_limit))}sec_{str(start_time)}.xlsx"
    #     df.to_excel(filename, header=column_names)
    filename = f"Test_{str(count)}.xlsx"
    # df.to_excel(filename, header=column_names)


try:
    # Define the file path for the count
    execution_count_file = 'Count.txt'

    # Check if the count file exists, and if not, create it and initialize the count to 0
    if not os.path.exists(execution_count_file):
        with open(execution_count_file, 'w') as f:
            f.write('0')

    # Read the current count from the file
    with open(execution_count_file, 'r') as f:
        count = int(f.read())

    count += 1

    # Write the new count back to the file
    # with open(execution_count_file, 'w') as f:
    #     f.write(str(count))

    def update(i):
        data = ser.readline().decode()[0:][:-2].split(",")  # 2-1-0/5-4-3/8-7-6
        # print(float(data[14]), float(data[13]), float(data[12]), "--",
        #       float(data[14]) - error5[0], float(data[13]) - error5[1], float(data[12]) - error5[2])
        print(data)
        # print([abs(float(data[2])) - 9.8, -(abs(float(data[1])) - 9.8), abs(float(data[0])) - 9.8])
        dir_shift1 = np.array([float(data[2]) - error1[0],
                               -(float(data[1]) - error1[1]),
                               float(data[0]) - error1[2]])
        # for i in range(3):
        #     if float(dir_shift1[i]) > 9.8:
        #         dir_shift1[i] = str(9.8)
        #     if float(dir_shift1[i]) < -9.8:
        #         dir_shift1[i] = str(-9.8)
        # print(dir_shift1)
        dir_shift2 = np.array([float(data[5]) - error2[0],
                               -(float(data[4]) - error2[1]),
                               float(data[3]) - error2[2]])
        # for i in range(3):
        #     if float(dir_shift1[i]) > 9.8:
        #         dir_shift1[i] = str(9.8)
        #     if float(dir_shift1[i]) < -9.8:
        #         dir_shift1[i] = str(-9.8)
        dir_shift3 = np.array([float(data[8]) - error3[0],
                               -(float(data[7]) - error3[1]),
                               float(data[6]) - error3[2]])
        # for i in range(3):
        #     if float(dir_shift1[i]) > 9.8:
        #         dir_shift1[i] = str(9.8)
        #     if float(dir_shift1[i]) < -9.8:
        #         dir_shift1[i] = str(-9.8)
        dir_shift4 = np.array([float(data[11]) - error4[0],
                               -(float(data[10]) - error4[1]),
                               float(data[9]) - error4[2]])
        # for i in range(3):
        #     if float(dir_shift1[i]) > 9.8:
        #         dir_shift1[i] = str(9.8)
        #     if float(dir_shift1[i]) < -9.8:
        #         dir_shift1[i] = str(-9.8)
        dir_shift5 = np.array([float(data[14]) - error5[0],
                               -(float(data[13]) - error5[1]),
                               float(data[12]) - error5[2]])
        # for i in range(3):
        #     if float(dir_shift1[i]) > 9.8:
        #         dir_shift1[i] = str(9.8)
        #     if float(dir_shift1[i]) < -9.8:
        #         dir_shift1[i] = str(-9.8)
        move_arrow(pos1,dir1 + dir_shift1,
                   # dir2 + dir_shift2,dir3 + dir_shift3,dir4 + dir_shift4,dir5 + dir_shift5,
                   trunk_plt1,
                   # trunk_plt2, trunk_plt3, trunk_plt4, trunk_plt5,
                   length_trunk)
        return [trunk_plt1,
                # trunk_plt2, trunk_plt3, trunk_plt4, trunk_plt5,line_plt,
                Angle1,
                # Angle2, Angle3, Angle4, Angle5
                ]

    ani = animation.FuncAnimation(fig, update, frames=None, interval=10, repeat=False, blit=True)
    plt.show()
    export()
    # if time.time() - start_time >= time_limit:
    #     export()
    #     break

except KeyboardInterrupt or InterruptedError:
    export()
