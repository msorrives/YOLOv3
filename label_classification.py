import cv2
import os
import glob
import fileinput
import numpy
#import numpy as np
import shutil
import random
import argparse

for filename in glob.glob('docs/Prueba_Labels/*.txt'):
        name, extension = os.path.splitext(os.path.basename(filename))
        file_name = name + extension
        print(name)
        #print (file_name)
        i = 0
        with open(filename, "r") as f:
                line = f.readline()
                if "harbor" in line:
                        print("Hay clase harbor")
                        continue
                elif "bridge" in line:
                        print("Hay clase bridge")
                        continue
                elif "swimming-pool" in line:
                        print("Hay clase swimming-pool")
                        continue
                elif "ground-track-field" in line:
                        print("Hay clase ground-track-field")
                        continue
                elif "soccer-ball-field" in line:
                        print("Hay clase soccer-ball-field")
                        continue
                elif "tennis-court" in line:
                        print("Hay clase tennis-court")
                        continue
                elif "basketball-court" in line:
                        print("Hay clase basketball-court")
                        continue
                elif "roundabout" in line:
                        print("Hay clase roundabout")
                        continue
                elif "baseball-diamond" in line:
                        print("Hay clase baseball-diamond")
                        continue
                elif "storage-tank" in line:
                        print("Hay clase storage-tank")
                        continue
                else:
                        print("No hay clase para eliminar")
                        print(line)

                        line1 = str(line)
                        line2 = line1[:-1]

                        path = "/root/workspace/YOLOV3/data/dataset/train/" + file_name + " "

                        filename1 = open('docs/Prueba_Labels_Classification/' + file_name, 'w').write(path + line2)

                while line:
                        line = f.readline()
                        if not line:
                                continue
                        elif "harbor" in line:
                                print("Hay clase harbor")
                                continue
                        elif "bridge" in line:
                                print("Hay clase bridge")
                                continue
                        elif "swimming-pool" in line:
                                print("Hay clase swimming-pool")
                                continue
                        elif "ground-track-field" in line:
                                print("Hay clase ground-track-field")
                                continue
                        elif "soccer-ball-field" in line:
                                print("Hay clase soccer-ball-field")
                                continue
                        elif "tennis-court" in line:
                                print("Hay clase tennis-court")
                                continue
                        elif "basketball-court" in line:
                                print("Hay clase basketball-court")
                                continue
                        elif "roundabout" in line:
                                print("Hay clase roundabout")
                                continue
                        elif "baseball-diamond" in line:
                                print("Hay clase baseball-diamond")
                                continue
                        elif "storage-tank" in line:
                                print("Hay clase storage-tank")
                                continue
                        else:
                                print("No hay clase para eliminar")
                                print(line)

                                if file_name in glob.glob('docs/Prueba_Labels'):

                                        line1 = str(line)
                                        line2 = line1[:-1]

                                        path = "/root/workspace/YOLOV3/data/dataset/train/" + file_name + " "

                                        filename1 = open('docs/Prueba_Labels_Classification/' + file_name, 'w').write(path + line2)

                                else:
                                        line1 = str(line)
                                        line2 = line1[:-1]

                                        filename1 = open('docs/Prueba_Labels_Classification/' + file_name, 'a').write(line2)
