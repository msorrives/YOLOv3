import cv2
import os
import glob
import fileinput
import numpy
#import numpy as np
import shutil
import random
import argparse

for filename in glob.glob('docs/DOTA29_Prueba_Labels/*.txt'):
        name, extension = os.path.splitext(os.path.basename(filename))
        file_name = name + extension
        print(name)
        print (file_name)
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
                        line1 = line.split(" ")


                        print(line1[9])
                        line = line.replace(line1[9], ',')
                        filename1 = open('docs/Prueba_Labels/' + file_name, 'w')
                        filename1.write("/root/workspace/YOLOV3/data/dataset/test/ " + line)

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
                                line1 = line.split(" ")
                                print(line1[9])
                                line = line.replace(line1[9], '')
                                line = line.replace(" ", ",")
                                filename1 = open('docs/Prueba_Labels/' + file_name, 'a')
                                filename1.write(line)


                                # for img in glob.glob('docs/Prueba/*.png'):
                                #        cv2.imread(img)
                                #        name, extension = os.path.splitext(os.path.basename(img))
                                #        name1 = name.split("_")
                                #        basename = name1[0]
                                #        print(name)
                                #        print(name1)
                                #        print(name1[0])
                                #        print("y")
                                #        print(name1[1])
                                #        print("x")
                                #        print(name1[2])
                                #        # file1 = open(file, 'r')
                                #        # print (file1.readlines())
                                #        print("Hola1")

                                #        # files = glob.glob('docs/DOTA29_Prueba_Labels/*.txt')
                                #        # print(files)

                                #        for fle in glob.glob('docs/DOTA29_Prueba_Labels/*.txt'):
                                #                print("Hola12")

                                #                print(fle)
                                #                # if basename ==

                                #                with open(fle, "r") as f:
                                #                        print("Hola13")
                                #                        text = f.read()
                                #                        print(len(text))
                                #                print(text)

                                #        # f = open("docs/DOTA29_Prueba_Labels/P0000.txt","r")
                                #        # f1 = f.readlines()
                                #        # for x in f1:
                                #        #        print(x)
                                #
                                #        # for files in glob.glob('docs/DOTA29_Prueba_Labels/*.txt'):
                                #        #        print("Hola2")
                                #        #        inputfile = open(files)
                                #        #        print(inputfile)
                                #        #        print("Hola3")
                                #        #        name_file, extension_file = os.path.splitext(os.path.basename(f))
                                #        #        print(name_file)
                                #        #        if basename == name_file:
                                #        #                print("Hola4")
