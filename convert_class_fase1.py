import cv2
import os
import glob
import fileinput
import numpy
#import numpy as np
import shutil
import random
import argparse

for filename in glob.glob('data/dataset/labels_class_convert/*.txt'):
    name, extension = os.path.splitext(os.path.basename(filename))
    file_name = name + extension
    print(name)

    with open(filename, "r") as f:
        line = f.readline()

        smallVehicle = "small-vehicle"
        largeVehicle = "large-vehicle"
        helicopter = "helicopter"
        plane = "plane"
        ship = "ship"

        if smallVehicle in line:
            print("Hay clase small-vehicle")
            print(line.replace("small-vehicle", "0"))
            line1 = line.replace("small-vehicle", "0")
            filename1 = open('data/dataset/labels_class_convert/' + file_name, 'w').write(line1)
            continue

        elif largeVehicle in line:
            print("Hay clase large-vehicle")
            print(line.replace("large-vehicle", "1"))
            line1 = line.replace("large-vehicle", "1")
            filename1 = open('data/dataset/labels_class_convert/' + file_name, 'w').write(line1)
            continue

        elif helicopter in line:
            print("Hay clase helicopter")
            print(line.replace("helicopter", "2"))
            line1 = line.replace("helicopter", "2")
            filename1 = open('data/dataset/labels_class_convert/' + file_name, 'w').write(line1)
            continue

        elif plane in line:
            print("Hay clase plane")
            print(line.replace("plane", "3"))
            line1 = line.replace("plane", "3")
            filename1 = open('data/dataset/labels_class_convert/' + file_name, 'w').write(line1)
            continue

        elif ship in line:
            print("Hay clase ship")
            print(line.replace("ship", "4"))
            line1 = line.replace("ship", "4")
            filename1 = open('data/dataset/labels_class_convert/' + file_name, 'w').write(line1)
            continue

        f.close()