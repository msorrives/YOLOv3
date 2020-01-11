import cv2
import os
import glob
import fileinput
import numpy
#import numpy as np
import shutil
import random
import argparse

for filename in glob.glob('data/dataset/labels_classification/*.txt'):

        name, extension = os.path.splitext(os.path.basename(filename))
        file_name = name + extension
        file_img = name + ".png"
        print(name)
        #print (file_name)

        with open(filename, "r") as f:
                line = f.readline()

                if "small-vehicle" in line:
                        print("Hay clase small-vehicle")
                        print(line.replace("small-vehicle","0"))
                        line1 = line.replace("small-vehicle","0")
                        open('data/dataset/labels_class_convert/' + file_name, 'w').write(line1)
                        continue
                elif "large-vehicle" in line:
                        print("Hay clase large-vehicle")
                        print(line.replace("large-vehicle", "1"))
                        line1 = line.replace("large-vehicle", "1")
                        open('data/dataset/labels_class_convert/' + file_name, 'w').write(line1)
                        continue
                elif "helicopter" in line:
                        print("Hay clase helicopter")
                        print(line.replace("helicopter", "2"))
                        line1 = line.replace("helicopter", "2")
                        open('data/dataset/labels_class_convert/' + file_name, 'w').write(line1)
                        continue
                elif "plane" in line:
                        print("Hay clase plane")
                        print(line.replace("plane", "3"))
                        line1 = line.replace("plane", "3")
                        open('data/dataset/labels_class_convert/' + file_name, 'w').write(line1)
                        continue
                elif "ship" in line:
                        print("Hay clase ship")
                        print(line.replace("ship", "4"))
                        line1 = line.replace("ship", "4")
                        open('data/dataset/labels_class_convert/' + file_name, 'w').write(line1)
                        continue
                else:
                        print("No hay clase para eliminar")
                        print(line)

                while line:
                        line = f.readline()

                        if not line:
                                continue
                        elif "small-vehicle" in line:
                            print("Hay clase small-vehicle")
                            print(line.replace("small-vehicle", "0"))
                            line1 = line.replace("small-vehicle", "0")
                            open('data/dataset/labels_class_convert/' + file_name, 'w').write(line1)
                            continue
                        elif "large-vehicle" in line:
                            print("Hay clase large-vehicle")
                            print(line.replace("large-vehicle", "1"))
                            line1 = line.replace("large-vehicle", "1")
                            open('data/dataset/labels_class_convert/' + file_name, 'w').write(line1)
                            continue
                        elif "helicopter" in line:
                            print("Hay clase helicopter")
                            print(line.replace("helicopter", "2"))
                            line1 = line.replace("helicopter", "2")
                            open('data/dataset/labels_class_convert/' + file_name, 'w').write(line1)
                            continue
                        elif "plane" in line:
                            print("Hay clase plane")
                            print(line.replace("plane", "3"))
                            line1 = line.replace("plane", "3")
                            open('data/dataset/labels_class_convert/' + file_name, 'w').write(line1)
                            continue
                        elif "ship" in line:
                            print("Hay clase ship")
                            print(line.replace("ship", "4"))
                            line1 = line.replace("ship", "4")
                            open('data/dataset/labels_class_convert/' + file_name, 'w').write(line1)
                            continue
                        else:
                            print("No hay clase para eliminar")
                            print(line)

                f.close()

