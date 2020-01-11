import cv2
import os
import glob
import fileinput
import numpy
#import numpy as np
import shutil
import random
import argparse

for img in glob.glob('data/dataset/train/*.png'):
        cv2.imread(img)
        img_name, img_extension = os.path.splitext(os.path.basename(img))
        name1 = img_name.split("_")
        basename = name1[0]
        basename1 = name1[1]
        basename2 = name1[2]

        print("bucle filename for") 

        for filename in glob.glob('data/dataset/labels_original/*.txt'):
                text_name, text_extension = os.path.splitext(os.path.basename(filename))
                file_name = text_name + text_extension
                label_name = img_name + text_extension

                if basename == text_name:
                        print("Coincide imagen "+basename+" con text "+text_name)
                        print(img_name)
                        print(basename1)
                        print(basename2)

                        # Y = 0

                        if basename1 == "0" and basename2 == "0":
                                print("basey == 0 and basex == 0")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if PosX1 < 416 and PosY1 < 416 and PosX2 < 416 and PosY2 < 416 and PosX3 < 416 and PosY3 < 416 and PosX4 < 416 and PosY4 < 416:
                                                print("Replace? 1")
                                                coord_X = PosX1
                                                coord_Y = PosY1
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:

                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if PosX1 < 416 and PosY1 < 416 and PosX2 < 416 and PosY2 < 416 and PosX3 < 416 and PosY3 < 416 and PosX4 < 416 and PosY4 < 416:
                                                        print("Replace? 2")
                                                        coord_X = PosX1
                                                        coord_Y = PosY1
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name,'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name,'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "0" and basename2 == "416":
                                print("basey == 0 and basex == 416")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        print("Replace?")
                                        if 416 < PosX1 < 832 and PosY1 < 416 and 416 < PosX2 < 832 and PosY2 < 416 and 416 < PosX3 < 832 and PosY3 < 416 and 416 < PosX4 < 832 and PosY4 < 416:

                                                print("Replace? 1")
                                                coord_X = PosX1 - 416
                                                coord_Y = PosY1
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                print("Replace??")
                                                if 416 < PosX1 < 832 and PosY1 < 416 and 416 < PosX2 < 832 and PosY2 < 416 and 416 < PosX3 < 832 and PosY3 < 416 and 416 < PosX4 < 832 and PosY4 < 416:

                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 416
                                                        coord_Y = PosY1
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "0" and basename2 == "832":
                                print("basey == 0 and basex == 832")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 832 < PosX1 < 1248 and PosY1 < 416 and 832 < PosX2 < 1248 and PosY2 < 416 and 832 < PosX3 < 1248 and PosY3 < 416 and 832 < PosX4 < 1248 and PosY4 < 416:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 832
                                                coord_Y = PosY1
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 832 < PosX1 < 1248 and PosY1 < 416 and 832 < PosX2 < 1248 and PosY2 < 416 and 832 < PosX3 < 1248 and PosY3 < 416 and 832 < PosX4 < 1248 and PosY4 < 416:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 832
                                                        coord_Y = PosY1
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "0" and basename2 == "1248":
                                print("basey == 0 and basex == 1248")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 1248 < PosX1 < 1664 and PosY1 < 416 and 1248 < PosX2 < 1664 and PosY2 < 416 and 1248 < PosX3 < 1664 and PosY3 < 416 and 1248 < PosX4 < 1664 and PosY4 < 416:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 1248
                                                coord_Y = PosY1
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write( new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 1248 < PosX1 < 1664 and PosY1 < 416 and 1248 < PosX2 < 1664 and PosY2 < 416 and 1248 < PosX3 < 1664 and PosY3 < 416 and 1248 < PosX4 < 1664 and PosY4 < 416:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 1248
                                                        coord_Y = PosY1
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "0" and basename2 == "1664":
                                print("basey == 0 and basex == 1664")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        print("Replace?")
                                        if 1664 < PosX1 < 2080 and PosY1 < 416 and 1664 < PosX2 < 2080 and PosY2 < 416 and 1664 < PosX3 < 2080 and PosY3 < 416 and 1664 < PosX4 < 2080 and PosY4 < 416:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 1664
                                                coord_Y = PosY1
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                print("Replace??")
                                                if 1664 < PosX1 < 2080 and PosY1 < 416 and 1664 < PosX2 < 2080 and PosY2 < 416 and 1664 < PosX3 < 2080 and PosY3 < 416 and 1664 < PosX4 < 2080 and PosY4 < 416:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 1664
                                                        coord_Y = PosY1
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                f.close()

                        elif basename1 == "0" and basename2 == "2080":
                                print("basey == 0 and basex == 2080")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 2080 < PosX1 < 2496 and PosY1 < 416 and 2080 < PosX2 < 2496 and PosY2 < 416 and 2080 < PosX3 < 2496 and PosY3 < 416 and 2080 < PosX4 < 2496 and PosY4 < 416:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 2080
                                                coord_Y = PosY1
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write( new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                print("Replace??")

                                                if 2080 < PosX1 < 2496 and PosY1 < 416 and 2080 < PosX2 < 2496 and PosY2 < 416 and 2080 < PosX3 < 2496 and PosY3 < 416 and 2080 < PosX4 < 2496 and PosY4 < 416:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 2080
                                                        coord_Y = PosY1
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge')                                                                :

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "0" and basename2 == "2496":
                                print("basey == 0 and basex == 2496")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        print("Replace?")
                                        if 2496 < PosX1 < 2912 and PosY1 < 416 and 2496 < PosX2 < 2912 and PosY2 < 416 and 2496 < PosX3 < 2912 and PosY3 < 416 and 2496 < PosX4 < 2912 and PosY4 < 416:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 2496
                                                coord_Y = PosY1
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write( new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                print("Replace??")
                                                if 2496 < PosX1 < 2912 and PosY1 < 416 and 2496 < PosX2 < 2912 and PosY2 < 416 and 2496 < PosX3 < 2912 and PosY3 < 416 and 2496 < PosX4 < 2912 and PosY4 < 416:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 2496
                                                        coord_Y = PosY1
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name,'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                f.close()

                        elif basename1 == "0" and basename2 == "2912":
                                print("basey == 0 and basex == 2912")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        print("Replace?")
                                        if 2912 < PosX1 < 3328 and PosY1 < 416 and 2912 < PosX2 < 3328 and PosY2 < 416 and 2912 < PosX3 < 3328 and PosY3 < 416 and 2912 < PosX4 < 3328 and PosY4 < 416:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 2912
                                                coord_Y = PosY1
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 2912 < PosX1 < 3328 and PosY1 < 416 and 2912 < PosX2 < 3328 and PosY2 < 416 and 2912 < PosX3 < 3328 and PosY3 < 416 and 2912 < PosX4 < 3328 and PosY4 < 416:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 2912
                                                        coord_Y = PosY1
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "0" and basename2 == "3328":
                                print("basey == 0 and basex == 3328")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        print("Replace?")

                                        if 3328 < PosX1 < 3744 and PosY1 < 416 and 3328 < PosX2 < 3744 and PosY2 < 416 and 3328 < PosX3 < 3744 and PosY3 < 416 and 3328 < PosX4 < 3744 and PosY4 < 416:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 3328
                                                coord_Y = PosY1
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write( new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                print("Replace??")
                                                if 3328 < PosX1 < 3744 and PosY1 < 416 and 3328 < PosX2 < 3744 and PosY2 < 416 and 3328 < PosX3 < 3744 and PosY3 < 416 and 3328 < PosX4 < 3744 and PosY4 < 416:

                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 3328
                                                        coord_Y = PosY1
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "0" and basename2 == "3744":
                                print("basey == 0 and basex == 3744")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        print("Replace?")

                                        if 3744 < PosX1 < 4160 and PosY1 < 416 and 3744 < PosX2 < 4160 and PosY2 < 416 and 3744 < PosX3 < 4160 and PosY3 < 416 and 3744 < PosX4 < 4160 and PosY4 < 416:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 3744
                                                coord_Y = PosY1
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 3744 < PosX1 < 4160 and PosY1 < 416 and 3744 < PosX2 < 4160 and PosY2 < 416 and 3744 < PosX3 < 4160 and PosY3 < 416 and 3744 < PosX4 < 4160 and PosY4 < 416:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 3744
                                                        coord_Y = PosY1
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        # Y = 416

                        elif basename1 == "416" and basename2 == "0":
                                print("basey == 416 and basex == 0")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        print("Replace?")

                                        if PosX1 < 416 and 416 < PosY1 < 832 and PosX2 < 416 and 416 < PosY2 < 832 and PosX3 < 416 and 416 < PosY3 < 832 and PosX4 < 416 and 416 < PosY4 < 832:
                                                print("Replace? 1")
                                                coord_X = PosX1
                                                coord_Y = PosY1 - 416
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write( new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if PosX1 < 416 and 416 < PosY1 < 832 and PosX2 < 416 and 416 < PosY2 < 832 and PosX3 < 416 and 416 < PosY3 < 832 and PosX4 < 416 and 416 < PosY4 < 832:
                                                        print("Replace? 2")
                                                        coord_X = PosX1
                                                        coord_Y = PosY1 - 416
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name,'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name,'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "416" and basename2 == "416":
                                print("basey == 416 and basex == 416")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        print("Replace?")

                                        if 416 < PosX1 < 832 and 416 < PosY1 < 832 and 416 < PosX2 < 832 and 416 < PosY2 < 832 and 416 < PosX3 < 832 and 416 < PosY3 < 832 and 416 < PosX4 < 832 and 416 < PosY4 < 832:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 416
                                                coord_Y = PosY1 - 416
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write( new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                print("Replace??")

                                                if 416 < PosX1 < 832 and 416 < PosY1 < 832 and 416 < PosX2 < 832 and 416 < PosY2 < 832 and 416 < PosX3 < 832 and 416 < PosY3 < 832 and 416 < PosX4 < 832 and 416 < PosY4 < 832:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 416
                                                        coord_Y = PosY1 - 416
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "416" and basename2 == "832":
                                print("basey == 416 and basex == 832")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 832 < PosX1 < 1248 and 416 < PosY1 < 832 and 832 < PosX2 < 1248 and 416 < PosY2 < 832 and 832 < PosX3 < 1248 and 416 < PosY3 < 832 and 832 < PosX4 < 1248 and 416 < PosY4 < 832:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 832
                                                coord_Y = PosY1 - 416
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                print("Replace??")

                                                if 832 < PosX1 < 1248 and 416 < PosY1 < 832 and 832 < PosX2 < 1248 and 416 < PosY2 < 832 and 832 < PosX3 < 1248 and 416 < PosY3 < 832 and 832 < PosX4 < 1248 and 416 < PosY4 < 832:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 832
                                                        coord_Y = PosY1 - 416
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "416" and basename2 == "1248":
                                print("basey == 416 and basex == 1248")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        print("Replace?")

                                        if 1248 < PosX1 < 1664 and 416 < PosY1 < 832 and 1248 < PosX2 < 1664 and 416 < PosY2 < 832 and 1248 < PosX3 < 1664 and 416 < PosY3 < 832 and 1248 < PosX4 < 1664 and 416 < PosY4 < 832:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 1248
                                                coord_Y = PosY1 - 416
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                print("Replace??")

                                                if 1248 < PosX1 < 1664 and 416 < PosY1 < 832 and 1248 < PosX2 < 1664 and 416 < PosY2 < 832 and 1248 < PosX3 < 1664 and 416 < PosY3 < 832 and 1248 < PosX4 < 1664 and 416 < PosY4 < 832:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 1248
                                                        coord_Y = PosY1 - 416
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "416" and basename2 == "1664":
                                print("basey == 416 and basex == 1664")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        print("Replace?")

                                        if 1664 < PosX1 < 2080 and 416 < PosY1 < 832 and 1664 < PosX2 < 2080 and 416 < PosY2 < 832 and 1664 < PosX3 < 2080 and 416 < PosY3 < 832 and 1664 < PosX4 < 2080 and 416 < PosY4 < 832:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 1664
                                                coord_Y = PosY1 - 416
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                print("Replace??")
                                                if 1664 < PosX1 < 2080 and 416 < PosY1 < 832 and 1664 < PosX2 < 2080 and 416 < PosY2 < 832 and 1664 < PosX3 < 2080 and 416 < PosY3 < 832 and 1664 < PosX4 < 2080 and 416 < PosY4 < 832:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 1664
                                                        coord_Y = PosY1 - 416
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "416" and basename2 == "2080":
                                print("basey == 416 and basex == 2080")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        print("Replace?")

                                        if 2080 < PosX1 < 2496 and 416 < PosY1 < 832 and 2080 < PosX2 < 2496 and 416 < PosY2 < 832 and 2080 < PosX3 < 2496 and 416 < PosY3 < 832 and 2080 < PosX4 < 2496 and 416 < PosY4 < 832:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 2080
                                                coord_Y = PosY1 - 416
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                print("Replace??")

                                                if 2080 < PosX1 < 2496 and 416 < PosY1 < 832 and 2080 < PosX2 < 2496 and 416 < PosY2 < 832 and 2080 < PosX3 < 2496 and 416 < PosY3 < 832 and 2080 < PosX4 < 2496 and 416 < PosY4 < 832:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 2080
                                                        coord_Y = PosY1 - 416
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "416" and basename2 == "2496":
                                print("basey == 416 and basex == 2496")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        print("Replace?")
                                        if 2496 < PosX1 < 2912 and 416 < PosY1 < 832 and 2496 < PosX2 < 2912 and 416 < PosY2 < 832 and 2496 < PosX3 < 2912 and 416 < PosY3 < 832 and 2496 < PosX4 < 2912 and 416 < PosY4 < 832:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 2496
                                                coord_Y = PosY1 - 416
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                print("Replace??")
                                                if 2496 < PosX1 < 2912 and 416 < PosY1 < 832 and 2496 < PosX2 < 2912 and 416 < PosY2 < 832 and 2496 < PosX3 < 2912 and 416 < PosY3 < 832 and 2496 < PosX4 < 2912 and 416 < PosY4 < 832:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 2496
                                                        coord_Y = PosY1 - 416
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                f.close()

                        elif basename1 == "416" and basename2 == "2912":
                                print("basey == 416 and basex == 2912")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        print("Replace?")
                                        if 2912 < PosX1 < 3328 and 416 < PosY1 < 832 and 2912 < PosX2 < 3328 and 416 < PosY2 < 832 and 2912 < PosX3 < 3328 and 416 < PosY3 < 832 and 2912 < PosX4 < 3328 and 416 < PosY4 < 832:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 2912
                                                coord_Y = PosY1 - 416
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                print("Replace??")
                                                if 2912 < PosX1 < 3328 and 416 < PosY1 < 832 and 2912 < PosX2 < 3328 and 416 < PosY2 < 832 and 2912 < PosX3 < 3328 and 416 < PosY3 < 832 and 2912 < PosX4 < 3328 and 416 < PosY4 < 832:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 2912
                                                        coord_Y = PosY1 - 416
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                f.close()

                        elif basename1 == "416" and basename2 == "3328":
                                print("basey == 416 and basex == 3328")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        print("Replace?")

                                        if 3328 < PosX1 < 3744 and 416 < PosY1 < 832 and 3328 < PosX2 < 3744 and 416 < PosY2 < 832 and 3328 < PosX3 < 3744 and 416 < PosY3 < 832 and 3328 < PosX4 < 3744 and 416 < PosY4 < 832:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 3328
                                                coord_Y = PosY1 - 416
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                print("Replace??")

                                                if 3328 < PosX1 < 3744 and 416 < PosY1 < 832 and 3328 < PosX2 < 3744 and 416 < PosY2 < 832 and 3328 < PosX3 < 3744 and 416 < PosY3 < 832 and 3328 < PosX4 < 3744 and 416 < PosY4 < 832:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 3328
                                                        coord_Y = PosY1 - 416
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                f.close()

                        elif basename1 == "416" and basename2 == "3744":
                                print("basey == 416 and basex == 3744")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        print("Replace?")

                                        if 3744 < PosX1 < 4160 and 416 < PosY1 < 832 and 3744 < PosX2 < 4160 and 416 < PosY2 < 832 and 3744 < PosX3 < 4160 and 416 < PosY3 < 832 and 3744 < PosX4 < 4160 and 416 < PosY4 < 832:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 3744
                                                coord_Y = PosY1 - 416
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 3744 < PosX1 < 4160 and 416 < PosY1 < 832 and 3744 < PosX2 < 4160 and 416 < PosY2 < 832 and 3744 < PosX3 < 4160 and 416 < PosY3 < 832 and 3744 < PosX4 < 4160 and 416 < PosY4 < 832:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 3744
                                                        coord_Y = PosY1 - 416
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                f.close()

                        # Y = 832

                        elif basename1 == "832" and basename2 == "0":
                                print("basey == 832 and basex == 0")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        print("Replace?")

                                        if PosX1 < 416 and 832 < PosY1 < 1248 and PosX2 < 416 and 832 < PosY2 < 1248 and PosX3 < 416 and 832 < PosY3 < 1248 and PosX4 < 416 and 832 < PosY4 < 1248:
                                                print("Replace? 1")
                                                coord_X = PosX1
                                                coord_Y = PosY1 - 832
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if PosX1 < 416 and 832 < PosY1 < 1248 and PosX2 < 416 and 832 < PosY2 < 1248 and PosX3 < 416 and 832 < PosY3 < 1248 and PosX4 < 416 and 832 < PosY4 < 1248:
                                                        print("Replace? 2")
                                                        coord_X = PosX1
                                                        coord_Y = PosY1 - 832
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                f.close()

                        elif basename1 == "832" and basename2 == "416":
                                print("basey == 832 and basex == 416")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 416 < PosX1 < 832 and 832 < PosY1 < 1248 and 416 < PosX2 < 832 and 832 < PosY2 < 1248 and 416 < PosX3 < 832 and 832 < PosY3 < 1248 and 416 < PosX4 < 832 and 832 < PosY4 < 1248:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 416
                                                coord_Y = PosY1 - 832
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 416 < PosX1 < 832 and 832 < PosY1 < 1248 and 416 < PosX2 < 832 and 832 < PosY2 < 1248 and 416 < PosX3 < 832 and 832 < PosY3 < 1248 and 416 < PosX4 < 832 and 832 < PosY4 < 1248:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 416
                                                        coord_Y = PosY1 - 832
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                f.close()

                        elif basename1 == "832" and basename2 == "832":
                                print("basey == 832 and basex == 832")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 832 < PosX1 < 1248 and 832 < PosY1 < 1248 and 832 < PosX2 < 1248 and 832 < PosY2 < 1248 and 832 < PosX3 < 1248 and 832 < PosY3 < 1248 and 832 < PosX4 < 1248 and 832 < PosY4 < 1248:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 832
                                                coord_Y = PosY1 - 832
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 832 < PosX1 < 1248 and 832 < PosY1 < 1248 and 832 < PosX2 < 1248 and 832 < PosY2 < 1248 and 832 < PosX3 < 1248 and 832 < PosY3 < 1248 and 832 < PosX4 < 1248 and 832 < PosY4 < 1248:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 832
                                                        coord_Y = PosY1 - 832
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                f.close()

                        elif basename1 == "832" and basename2 == "1248":
                                print("basey == 832 and basex == 1248")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 1248 < PosX1 < 1664 and 832 < PosY1 < 1248 and 1248 < PosX2 < 1664 and 832 < PosY2 < 1248 and 1248 < PosX3 < 1664 and 832 < PosY3 < 1248 and 1248 < PosX4 < 1664 and 832 < PosY4 < 1248:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 1248
                                                coord_Y = PosY1 - 832
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 1248 < PosX1 < 1664 and 832 < PosY1 < 1248 and 1248 < PosX2 < 1664 and 832 < PosY2 < 1248 and 1248 < PosX3 < 1664 and 832 < PosY3 < 1248 and 1248 < PosX4 < 1664 and 832 < PosY4 < 1248:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 1248
                                                        coord_Y = PosY1 - 832
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "832" and basename2 == "1664":
                                print("basey == 832 and basex == 1664")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 1664 < PosX1 < 2080 and 832 < PosY1 < 1248 and 1664 < PosX2 < 2080 and 832 < PosY2 < 1248 and 1664 < PosX3 < 2080 and 832 < PosY3 < 1248 and 1664 < PosX4 < 2080 and 832 < PosY4 < 1248:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 1664
                                                coord_Y = PosY1 - 832
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 1664 < PosX1 < 2080 and 832 < PosY1 < 1248 and 1664 < PosX2 < 2080 and 832 < PosY2 < 1248 and 1664 < PosX3 < 2080 and 832 < PosY3 < 1248 and 1664 < PosX4 < 2080 and 832 < PosY4 < 1248:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 1664
                                                        coord_Y = PosY1 - 832
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "832" and basename2 == "2080":
                                print("basey == 832 and basex == 2080")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 2080 < PosX1 < 2496 and 832 < PosY1 < 1248 and 2080 < PosX2 < 2496 and 832 < PosY2 < 1248 and 2080 < PosX3 < 2496 and 832 < PosY3 < 1248 and 2080 < PosX4 < 2496 and 832 < PosY4 < 1248:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 2080
                                                coord_Y = PosY1 - 832
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 2080 < PosX1 < 2496 and 832 < PosY1 < 1248 and 2080 < PosX2 < 2496 and 832 < PosY2 < 1248 and 2080 < PosX3 < 2496 and 832 < PosY3 < 1248 and 2080 < PosX4 < 2496 and 832 < PosY4 < 1248:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 2080
                                                        coord_Y = PosY1 - 832
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "832" and basename2 == "2496":
                                print("basey == 832 and basex == 2496")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 2496 < PosX1 < 2912 and 832 < PosY1 < 1248 and 2496 < PosX2 < 2912 and 832 < PosY2 < 1248 and 2496 < PosX3 < 2912 and 832 < PosY3 < 1248 and 2496 < PosX4 < 2912 and 832 < PosY4 < 1248:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 2496
                                                coord_Y = PosY1 - 832
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 2496 < PosX1 < 2912 and 832 < PosY1 < 1248 and 2496 < PosX2 < 2912 and 832 < PosY2 < 1248 and 2496 < PosX3 < 2912 and 832 < PosY3 < 1248 and 2496 < PosX4 < 2912 and 832 < PosY4 < 1248:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 2496
                                                        coord_Y = PosY1 - 832
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "832" and basename2 == "2912":
                                print("basey == 832 and basex == 2912")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                if 2912 < PosX1 < 3328 and 832 < PosY1 < 1248 and 2912 < PosX2 < 3328 and 832 < PosY2 < 1248 and 2912 < PosX3 < 3328 and 832 < PosY3 < 1248 and 2912 < PosX4 < 3328 and 832 < PosY4 < 1248:
                                        print("Replace? 1")
                                        coord_X = PosX1 - 2912
                                        coord_Y = PosY1 - 832
                                        coord_H = PosX2 - PosX1
                                        coord_W = PosY4 - PosY1

                                        print("Coordenadas x, y, h, w:")
                                        print(coord_X)
                                        print(coord_Y)
                                        print(str(float(coord_H)))
                                        print(str(float(coord_W)))

                                        print("Linia replaced: ")
                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                        print(new_list)

                                        new_line = ""

                                        for ele in new_list:
                                                new_line += str(ele) + ","

                                        print(new_line)

                                        filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 2912 < PosX1 < 3328 and 832 < PosY1 < 1248 and 2912 < PosX2 < 3328 and 832 < PosY2 < 1248 and 2912 < PosX3 < 3328 and 832 < PosY3 < 1248 and 2912 < PosX4 < 3328 and 832 < PosY4 < 1248:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 2912
                                                        coord_Y = PosY1 - 832
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "832" and basename2 == "3328":
                                print("basey == 832 and basex == 3328")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 3328 < PosX1 < 3744 and 832 < PosY1 < 1248 and 3328 < PosX2 < 3744 and 832 < PosY2 < 1248 and 3328 < PosX3 < 3744 and 832 < PosY3 < 1248 and 3328 < PosX4 < 3744 and 832 < PosY4 < 1248:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 3328
                                                coord_Y = PosY1 - 832
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 3328 < PosX1 < 3744 and 832 < PosY1 < 1248 and 3328 < PosX2 < 3744 and 832 < PosY2 < 1248 and 3328 < PosX3 < 3744 and 832 < PosY3 < 1248 and 3328 < PosX4 < 3744 and 832 < PosY4 < 1248:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 3328
                                                        coord_Y = PosY1 - 832
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "832" and basename2 == "3744":
                                print("basey == 832 and basex == 3744")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 3744 < PosX1 < 4160 and 832 < PosY1 < 1248 and 3744 < PosX2 < 4160 and 832 < PosY2 < 1248 and 3744 < PosX3 < 4160 and 832 < PosY3 < 1248 and 3744 < PosX4 < 4160 and 832 < PosY4 < 1248:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 3744
                                                coord_Y = PosY1 - 832
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 3744 < PosX1 < 4160 and 832 < PosY1 < 1248 and 3744 < PosX2 < 4160 and 832 < PosY2 < 1248 and 3744 < PosX3 < 4160 and 832 < PosY3 < 1248 and 3744 < PosX4 < 4160 and 832 < PosY4 < 1248:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 3744
                                                        coord_Y = PosY1 - 832
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        # Y = 1248

                        elif basename1 == "1248" and basename2 == "0":
                                print("basey == 1248 and basex == 0")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if PosX1 < 416 and 1248 < PosY1 < 1664 and PosX2 < 416 and 1248 < PosY2 < 1664 and PosX3 < 416 and 1248 < PosY3 < 1664 and PosX4 < 416 and 1248 < PosY4 < 1664:
                                                print("Replace? 1")
                                                coord_X = PosX1
                                                coord_Y = PosY1 - 1248
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if PosX1 < 416 and 1248 < PosY1 < 1664 and PosX2 < 416 and 1248 < PosY2 < 1664 and PosX3 < 416 and 1248 < PosY3 < 1664 and PosX4 < 416 and 1248 < PosY4 < 1664:
                                                        print("Replace? 2")
                                                        coord_X = PosX1
                                                        coord_Y = PosY1 - 1248
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "1248" and basename2 == "416":
                                print("basey == 1248 and basex == 416")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 416 < PosX1 < 832 and 1248 < PosY1 < 1664 and 416 < PosX2 < 832 and 1248 < PosY2 < 1664 and 416 < PosX3 < 832 and 1248 < PosY3 < 1664 and 416 < PosX4 < 832 and 1248 < PosY4 < 1664:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 416
                                                coord_Y = PosY1 - 1248
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 416 < PosX1 < 832 and 1248 < PosY1 < 1664 and 416 < PosX2 < 832 and 1248 < PosY2 < 1664 and 416 < PosX3 < 832 and 1248 < PosY3 < 1664 and 416 < PosX4 < 832 and 1248 < PosY4 < 1664:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 416
                                                        coord_Y = PosY1 - 1248
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "1248" and basename2 == "832":
                                print("basey == 1248 and basex == 832")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 832 < PosX1 < 1248 and 1248 < PosY1 < 1664 and 832 < PosX2 < 1248 and 1248 < PosY2 < 1664 and 832 < PosX3 < 1248 and 1248 < PosY3 < 1664 and 832 < PosX4 < 1248 and 1248 < PosY4 < 1664:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 832
                                                coord_Y = PosY1 - 1248
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 832 < PosX1 < 1248 and 1248 < PosY1 < 1664 and 832 < PosX2 < 1248 and 1248 < PosY2 < 1664 and 832 < PosX3 < 1248 and 1248 < PosY3 < 1664 and 832 < PosX4 < 1248 and 1248 < PosY4 < 1664:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 832
                                                        coord_Y = PosY1 - 1248
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "1248" and basename2 == "1248":
                                print("basey == 1248 and basex == 1248")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 1248 < PosX1 < 1664 and 1248 < PosY1 < 1664 and 1248 < PosX2 < 1664 and 1248 < PosY2 < 1664 and 1248 < PosX3 < 1664 and 1248 < PosY3 < 1664 and 1248 < PosX4 < 1664 and 1248 < PosY4 < 1664:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 1248
                                                coord_Y = PosY1 - 1248
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 1248 < PosX1 < 1664 and 1248 < PosY1 < 1664 and 1248 < PosX2 < 1664 and 1248 < PosY2 < 1664 and 1248 < PosX3 < 1664 and 1248 < PosY3 < 1664 and 1248 < PosX4 < 1664 and 1248 < PosY4 < 1664:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 1248
                                                        coord_Y = PosY1 - 1248
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "1248" and basename2 == "1664":
                                print("basey == 1248 and basex == 1664")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 1664 < PosX1 < 2080 and 1248 < PosY1 < 1664 and 1664 < PosX2 < 2080 and 1248 < PosY2 < 1664 and 1664 < PosX3 < 2080 and 1248 < PosY3 < 1664 and 1664 < PosX4 < 2080 and 1248 < PosY4 < 1664:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 1664
                                                coord_Y = PosY1 - 1248
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 1664 < PosX1 < 2080 and 1248 < PosY1 < 1664 and 1664 < PosX2 < 2080 and 1248 < PosY2 < 1664 and 1664 < PosX3 < 2080 and 1248 < PosY3 < 1664 and 1664 < PosX4 < 2080 and 1248 < PosY4 < 1664:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 1664
                                                        coord_Y = PosY1 - 1248
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "1248" and basename2 == "2080":
                                print("basey == 1248 and basex == 2080")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 2080 < PosX1 < 2496 and 1248 < PosY1 < 1664 and 2080 < PosX2 < 2496 and 1248 < PosY2 < 1664 and 2080 < PosX3 < 2496 and 1248 < PosY3 < 1664 and 2080 < PosX4 < 2496 and 1248 < PosY4 < 1664:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 2080
                                                coord_Y = PosY1 - 1248
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 2080 < PosX1 < 2496 and 1248 < PosY1 < 1664 and 2080 < PosX2 < 2496 and 1248 < PosY2 < 1664 and 2080 < PosX3 < 2496 and 1248 < PosY3 < 1664 and 2080 < PosX4 < 2496 and 1248 < PosY4 < 1664:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 2080
                                                        coord_Y = PosY1 - 1248
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "1248" and basename2 == "2496":
                                print("basey == 1248 and basex == 2496")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 2496 < PosX1 < 2912 and 1248 < PosY1 < 1664 and 2496 < PosX2 < 2912 and 1248 < PosY2 < 1664 and 2496 < PosX3 < 2912 and 1248 < PosY3 < 1664 and 2496 < PosX4 < 2912 and 1248 < PosY4 < 1664:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 2496
                                                coord_Y = PosY1 - 1248
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 2496 < PosX1 < 2912 and 1248 < PosY1 < 1664 and 2496 < PosX2 < 2912 and 1248 < PosY2 < 1664 and 2496 < PosX3 < 2912 and 1248 < PosY3 < 1664 and 2496 < PosX4 < 2912 and 1248 < PosY4 < 1664:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 2496
                                                        coord_Y = PosY1 - 1248
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "1248" and basename2 == "2912":
                                print("basey == 1248 and basex == 2912")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 2912 < PosX1 < 3328 and 1248 < PosY1 < 1664 and 2912 < PosX2 < 3328 and 1248 < PosY2 < 1664 and 2912 < PosX3 < 3328 and 1248 < PosY3 < 1664 and 2912 < PosX4 < 3328 and 1248 < PosY4 < 1664:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 2912
                                                coord_Y = PosY1 - 1248
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 2912 < PosX1 < 3328 and 1248 < PosY1 < 1664 and 2912 < PosX2 < 3328 and 1248 < PosY2 < 1664 and 2912 < PosX3 < 3328 and 1248 < PosY3 < 1664 and 2912 < PosX4 < 3328 and 1248 < PosY4 < 1664:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 2912
                                                        coord_Y = PosY1 - 1248
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "1248" and basename2 == "3328":
                                print("basey == 1248 and basex == 3328")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 3328 < PosX1 < 3744 and 1248 < PosY1 < 1664 and 3328 < PosX2 < 3744 and 1248 < PosY2 < 1664 and 3328 < PosX3 < 3744 and 1248 < PosY3 < 1664 and 3328 < PosX4 < 3744 and 1248 < PosY4 < 1664:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 3328
                                                coord_Y = PosY1 - 1248
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 3328 < PosX1 < 3744 and 1248 < PosY1 < 1664 and 3328 < PosX2 < 3744 and 1248 < PosY2 < 1664 and 3328 < PosX3 < 3744 and 1248 < PosY3 < 1664 and 3328 < PosX4 < 3744 and 1248 < PosY4 < 1664:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 3328
                                                        coord_Y = PosY1 - 1248
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                f.close()

                        elif basename1 == "1248" and basename2 == "3744":
                                print("basey == 1248 and basex == 3744")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 3744 < PosX1 < 4160 and 1248 < PosY1 < 1664 and 3744 < PosX2 < 4160 and 1248 < PosY2 < 1664 and 3744 < PosX3 < 4160 and 1248 < PosY3 < 1664 and 3744 < PosX4 < 4160 and 1248 < PosY4 < 1664:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 3744
                                                coord_Y = PosY1 - 1248
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 3744 < PosX1 < 4160 and 1248 < PosY1 < 1664 and 3744 < PosX2 < 4160 and 1248 < PosY2 < 1664 and 3744 < PosX3 < 4160 and 1248 < PosY3 < 1664 and 3744 < PosX4 < 4160 and 1248 < PosY4 < 1664:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 3744
                                                        coord_Y = PosY1 - 1248
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                f.close()

                        # Y = 1664

                        elif basename1 == "1664" and basename2 == "0":
                                print("basey == 1664 and basex == 0")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if PosX1 < 416 and 1664 < PosY1 < 2080 and PosX2 < 416 and 1664 < PosY2 < 2080 and PosX3 < 416 and 1664 < PosY3 < 2080 and PosX4 < 416 and 1664 < PosY4 < 2080:
                                                print("Replace? 1")
                                                coord_X = PosX1
                                                coord_Y = PosY1 - 1664
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if PosX1 < 416 and 1664 < PosY1 < 2080 and PosX2 < 416 and 1664 < PosY2 < 2080 and PosX3 < 416 and 1664 < PosY3 < 2080 and PosX4 < 416 and 1664 < PosY4 < 2080:
                                                        print("Replace? 2")
                                                        coord_X = PosX1
                                                        coord_Y = PosY1 - 1664
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "1664" and basename2 == "416":
                                print("basey == 1664 and basex == 416")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 416 < PosX1 < 832 and 1664 < PosY1 < 2080 and 416 < PosX2 < 832 and 1664 < PosY2 < 2080 and 416 < PosX3 < 832 and 1664 < PosY3 < 2080 and 416 < PosX4 < 832 and 1664 < PosY4 < 2080:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 416
                                                coord_Y = PosY1 - 1664
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 416 < PosX1 < 832 and 1664 < PosY1 < 2080 and 416 < PosX2 < 832 and 1664 < PosY2 < 2080 and 416 < PosX3 < 832 and 1664 < PosY3 < 2080 and 416 < PosX4 < 832 and 1664 < PosY4 < 2080:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 416
                                                        coord_Y = PosY1 - 1664
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "1664" and basename2 == "832":
                                print("basey == 1664 and basex == 832")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 832 < PosX1 < 1248 and 1664 < PosY1 < 2080 and 832 < PosX2 < 1248 and 1664 < PosY2 < 2080 and 832 < PosX3 < 1248 and 1664 < PosY3 < 2080 and 832 < PosX4 < 1248 and 1664 < PosY4 < 2080:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 832
                                                coord_Y = PosY1 - 1664
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 832 < PosX1 < 1248 and 1664 < PosY1 < 2080 and 832 < PosX2 < 1248 and 1664 < PosY2 < 2080 and 832 < PosX3 < 1248 and 1664 < PosY3 < 2080 and 832 < PosX4 < 1248 and 1664 < PosY4 < 2080:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 832
                                                        coord_Y = PosY1 - 1664
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "1664" and basename2 == "1248":
                                print("basey == 1664 and basex == 1248")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 1248 < PosX1 < 1664 and 1664 < PosY1 < 2080 and 1248 < PosX2 < 1664 and 1664 < PosY2 < 2080 and 1248 < PosX3 < 1664 and 1664 < PosY3 < 2080 and 1248 < PosX4 < 1664 and 1664 < PosY4 < 2080:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 1248
                                                coord_Y = PosY1 - 1664
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 1248 < PosX1 < 1664 and 1664 < PosY1 < 2080 and 1248 < PosX2 < 1664 and 1664 < PosY2 < 2080 and 1248 < PosX3 < 1664 and 1664 < PosY3 < 2080 and 1248 < PosX4 < 1664 and 1664 < PosY4 < 2080:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 1248
                                                        coord_Y = PosY1 - 1664
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "1664" and basename2 == "1664":
                                print("basey == 1664 and basex == 1664")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 1664 < PosX1 < 2080 and 1664 < PosY1 < 2080 and 1664 < PosX2 < 2080 and 1664 < PosY2 < 2080 and 1664 < PosX3 < 2080 and 1664 < PosY3 < 2080 and 1664 < PosX4 < 2080 and 1664 < PosY4 < 2080:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 1664
                                                coord_Y = PosY1 - 1664
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 1664 < PosX1 < 2080 and 1664 < PosY1 < 2080 and 1664 < PosX2 < 2080 and 1664 < PosY2 < 2080 and 1664 < PosX3 < 2080 and 1664 < PosY3 < 2080 and 1664 < PosX4 < 2080 and 1664 < PosY4 < 2080:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 1664
                                                        coord_Y = PosY1 - 1664
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "1664" and basename2 == "2080":
                                print("basey == 1664 and basex == 2080")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 2080 < PosX1 < 2496 and 1664 < PosY1 < 2080 and 2080 < PosX2 < 2496 and 1664 < PosY2 < 2080 and 2080 < PosX3 < 2496 and 1664 < PosY3 < 2080 and 2080 < PosX4 < 2496 and 1664 < PosY4 < 2080:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 2080
                                                coord_Y = PosY1 - 1664
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 2080 < PosX1 < 2496 and 1664 < PosY1 < 2080 and 2080 < PosX2 < 2496 and 1664 < PosY2 < 2080 and 2080 < PosX3 < 2496 and 1664 < PosY3 < 2080 and 2080 < PosX4 < 2496 and 1664 < PosY4 < 2080:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 2080
                                                        coord_Y = PosY1 - 1664
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "1664" and basename2 == "2496":
                                print("basey == 1664 and basex == 2496")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 2496 < PosX1 < 2912 and 1664 < PosY1 < 2080 and 2496 < PosX2 < 2912 and 1664 < PosY2 < 2080 and 2496 < PosX3 < 2912 and 1664 < PosY3 < 2080 and 2496 < PosX4 < 2912 and 1664 < PosY4 < 2080:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 2496
                                                coord_Y = PosY1 - 1664
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 2496 < PosX1 < 2912 and 1664 < PosY1 < 2080 and 2496 < PosX2 < 2912 and 1664 < PosY2 < 2080 and 2496 < PosX3 < 2912 and 1664 < PosY3 < 2080 and 2496 < PosX4 < 2912 and 1664 < PosY4 < 2080:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 2496
                                                        coord_Y = PosY1 - 1664
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "1664" and basename2 == "2912":
                                print("basey == 1664 and basex == 2912")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 2912 < PosX1 < 3328 and 1664 < PosY1 < 2080 and 2912 < PosX2 < 3328 and 1664 < PosY2 < 2080 and 2912 < PosX3 < 3328 and 1664 < PosY3 < 2080 and 2912 < PosX4 < 3328 and 1664 < PosY4 < 2080:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 2912
                                                coord_Y = PosY1 - 1664
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 2912 < PosX1 < 3328 and 1664 < PosY1 < 2080 and 2912 < PosX2 < 3328 and 1664 < PosY2 < 2080 and 2912 < PosX3 < 3328 and 1664 < PosY3 < 2080 and 2912 < PosX4 < 3328 and 1664 < PosY4 < 2080:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 2912
                                                        coord_Y = PosY1 - 1664
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "1664" and basename2 == "3328":
                                print("basey == 1664 and basex == 3328")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 3328 < PosX1 < 3744 and 1664 < PosY1 < 2080 and 3328 < PosX2 < 3744 and 1664 < PosY2 < 2080 and 3328 < PosX3 < 3744 and 1664 < PosY3 < 2080 and 3328 < PosX4 < 3744 and 1664 < PosY4 < 2080:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 3328
                                                coord_Y = PosY1 - 1664
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 3328 < PosX1 < 3744 and 1664 < PosY1 < 2080 and 3328 < PosX2 < 3744 and 1664 < PosY2 < 2080 and 3328 < PosX3 < 3744 and 1664 < PosY3 < 2080 and 3328 < PosX4 < 3744 and 1664 < PosY4 < 2080:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 3328
                                                        coord_Y = PosY1 - 1664
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "1664" and basename2 == "3744":
                                print("basey == 1664 and basex == 3744")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 3744 < PosX1 < 4160 and 1664 < PosY1 < 2080 and 3744 < PosX2 < 4160 and 1664 < PosY2 < 2080 and 3744 < PosX3 < 4160 and 1664 < PosY3 < 2080 and 3744 < PosX4 < 4160 and 1664 < PosY4 < 2080:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 3744
                                                coord_Y = PosY1 - 1664
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 3744 < PosX1 < 4160 and 1664 < PosY1 < 2080 and 3744 < PosX2 < 4160 and 1664 < PosY2 < 2080 and 3744 < PosX3 < 4160 and 1664 < PosY3 < 2080 and 3744 < PosX4 < 4160 and 1664 < PosY4 < 2080:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 3744
                                                        coord_Y = PosY1 - 1664
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        # Y = 2080

                        elif basename1 == "2080" and basename2 == "0":
                                print("basey == 2080 and basex == 0")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if PosX1 < 416 and 2080 < PosY1 < 2496 and PosX2 < 416 and 2080 < PosY2 < 2496 and PosX3 < 416 and 2080 < PosY3 < 2496 and PosX4 < 416 and 2080 < PosY4 < 2496:
                                                print("Replace? 1")
                                                coord_X = PosX1
                                                coord_Y = PosY1 - 2080
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if PosX1 < 416 and 2080 < PosY1 < 2496 and PosX2 < 416 and 2080 < PosY2 < 2496 and PosX3 < 416 and 2080 < PosY3 < 2496 and PosX4 < 416 and 2080 < PosY4 < 2496:
                                                        print("Replace? 2")
                                                        coord_X = PosX1
                                                        coord_Y = PosY1 - 2080
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "2080" and basename2 == "416":
                                print("basey == 2080 and basex == 416")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 416 < PosX1 < 832 and 2080 < PosY1 < 2496 and 416 < PosX2 < 832 and 2080 < PosY2 < 2496 and 416 < PosX3 < 832 and 2080 < PosY3 < 2496 and 416 < PosX4 < 832 and 2080 < PosY4 < 2496:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 416
                                                coord_Y = PosY1 - 2080
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 416 < PosX1 < 832 and 2080 < PosY1 < 2496 and 416 < PosX2 < 832 and 2080 < PosY2 < 2496 and 416 < PosX3 < 832 and 2080 < PosY3 < 2496 and 416 < PosX4 < 832 and 2080 < PosY4 < 2496:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 416
                                                        coord_Y = PosY1 - 2080
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "2080" and basename2 == "832":
                                print("basey == 2080 and basex == 832")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 832 < PosX1 < 1248 and 2080 < PosY1 < 2496 and 832 < PosX2 < 1248 and 2080 < PosY2 < 2496 and 832 < PosX3 < 1248 and 2080 < PosY3 < 2496 and 832 < PosX4 < 1248 and 2080 < PosY4 < 2496:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 832
                                                coord_Y = PosY1 - 2080
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 832 < PosX1 < 1248 and 2080 < PosY1 < 2496 and 832 < PosX2 < 1248 and 2080 < PosY2 < 2496 and 832 < PosX3 < 1248 and 2080 < PosY3 < 2496 and 832 < PosX4 < 1248 and 2080 < PosY4 < 2496:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 832
                                                        coord_Y = PosY1 - 2080
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "2080" and basename2 == "1248":
                                print("basey == 2080 and basex == 1248")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 1248 < PosX1 < 1664 and 2080 < PosY1 < 2496 and 1248 < PosX2 < 1664 and 2080 < PosY2 < 2496 and 1248 < PosX3 < 1664 and 2080 < PosY3 < 2496 and 1248 < PosX4 < 1664 and 2080 < PosY4 < 2496:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 1248
                                                coord_Y = PosY1 - 2080
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 1248 < PosX1 < 1664 and 2080 < PosY1 < 2496 and 1248 < PosX2 < 1664 and 2080 < PosY2 < 2496 and 1248 < PosX3 < 1664 and 2080 < PosY3 < 2496 and 1248 < PosX4 < 1664 and 2080 < PosY4 < 2496:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 1248
                                                        coord_Y = PosY1 - 2080
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "2080" and basename2 == "1664":
                                print("basey == 2080 and basex == 1664")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 1664 < PosX1 < 2080 and 2080 < PosY1 < 2496 and 1664 < PosX2 < 2080 and 2080 < PosY2 < 2496 and 1664 < PosX3 < 2080 and 2080 < PosY3 < 2496 and 1664 < PosX4 < 2080 and 2080 < PosY4 < 2496:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 1664
                                                coord_Y = PosY1 - 2080
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 1664 < PosX1 < 2080 and 2080 < PosY1 < 2496 and 1664 < PosX2 < 2080 and 2080 < PosY2 < 2496 and 1664 < PosX3 < 2080 and 2080 < PosY3 < 2496 and 1664 < PosX4 < 2080 and 2080 < PosY4 < 2496:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 1664
                                                        coord_Y = PosY1 - 2080
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "2080" and basename2 == "2080":
                                print("basey == 2080 and basex == 2080")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 2080 < PosX1 < 2496 and 2080 < PosY1 < 2496 and 2080 < PosX2 < 2496 and 2080 < PosY2 < 2496 and 2080 < PosX3 < 2496 and 2080 < PosY3 < 2496 and 2080 < PosX4 < 2496 and 2080 < PosY4 < 2496:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 2080
                                                coord_Y = PosY1 - 2080
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 2080 < PosX1 < 2496 and 2080 < PosY1 < 2496 and 2080 < PosX2 < 2496 and 2080 < PosY2 < 2496 and 2080 < PosX3 < 2496 and 2080 < PosY3 < 2496 and 2080 < PosX4 < 2496 and 2080 < PosY4 < 2496:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 2080
                                                        coord_Y = PosY1 - 2080
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "2080" and basename2 == "2496":
                                print("basey == 2080 and basex == 2496")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 2496 < PosX1 < 2912 and 2080 < PosY1 < 2496 and 2496 < PosX2 < 2912 and 2080 < PosY2 < 2496 and 2496 < PosX3 < 2912 and 2080 < PosY3 < 2496 and 2496 < PosX4 < 2912 and 2080 < PosY4 < 2496:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 2496
                                                coord_Y = PosY1 - 2080
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 2496 < PosX1 < 2912 and 2080 < PosY1 < 2496 and 2496 < PosX2 < 2912 and 2080 < PosY2 < 2496 and 2496 < PosX3 < 2912 and 2080 < PosY3 < 2496 and 2496 < PosX4 < 2912 and 2080 < PosY4 < 2496:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 2496
                                                        coord_Y = PosY1 - 2080
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "2080" and basename2 == "2912":
                                print("basey == 2080 and basex == 2912")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 2912 < PosX1 < 3328 and 2080 < PosY1 < 2496 and 2912 < PosX2 < 3328 and 2080 < PosY2 < 2496 and 2912 < PosX3 < 3328 and 2080 < PosY3 < 2496 and 2912 < PosX4 < 3328 and 2080 < PosY4 < 2496:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 2912
                                                coord_Y = PosY1 - 2080
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 2912 < PosX1 < 3328 and 2080 < PosY1 < 2496 and 2912 < PosX2 < 3328 and 2080 < PosY2 < 2496 and 2912 < PosX3 < 3328 and 2080 < PosY3 < 2496 and 2912 < PosX4 < 3328 and 2080 < PosY4 < 2496:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 2912
                                                        coord_Y = PosY1 - 2080
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "2080" and basename2 == "3328":
                                print("basey == 2080 and basex == 3328")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 3328 < PosX1 < 3744 and 2080 < PosY1 < 2496 and 3328 < PosX2 < 3744 and 2080 < PosY2 < 2496 and 3328 < PosX3 < 3744 and 2080 < PosY3 < 2496 and 3328 < PosX4 < 3744 and 2080 < PosY4 < 2496:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 3328
                                                coord_Y = PosY1 - 2080
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 3328 < PosX1 < 3744 and 2080 < PosY1 < 2496 and 3328 < PosX2 < 3744 and 2080 < PosY2 < 2496 and 3328 < PosX3 < 3744 and 2080 < PosY3 < 2496 and 3328 < PosX4 < 3744 and 2080 < PosY4 < 2496:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 3328
                                                        coord_Y = PosY1 - 2080
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "2080" and basename2 == "3744":
                                print("basey == 2080 and basex == 3744")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 3744 < PosX1 < 4160 and 2080 < PosY1 < 2496 and 3744 < PosX2 < 4160 and 2080 < PosY2 < 2496 and 3744 < PosX3 < 4160 and 2080 < PosY3 < 2496 and 3744 < PosX4 < 4160 and 2080 < PosY4 < 2496:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 3744
                                                coord_Y = PosY1 - 2080
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 3744 < PosX1 < 4160 and 2080 < PosY1 < 2496 and 3744 < PosX2 < 4160 and 2080 < PosY2 < 2496 and 3744 < PosX3 < 4160 and 2080 < PosY3 < 2496 and 3744 < PosX4 < 4160 and 2080 < PosY4 < 2496:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 3744
                                                        coord_Y = PosY1 - 2080
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        # Y = 2496

                        elif basename1 == "2496" and basename2 == "0":
                                print("basey == 2496 and basex == 0")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if PosX1 < 416 and 2496 < PosY1 < 2912 and PosX2 < 416 and 2496 < PosY2 < 2912 and PosX3 < 416 and 2496 < PosY3 < 2912 and PosX4 < 416 and 2496 < PosY4 < 2912:
                                                print("Replace? 1")
                                                coord_X = PosX1
                                                coord_Y = PosY1 - 2496
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if PosX1 < 416 and 2496 < PosY1 < 2912 and PosX2 < 416 and 2496 < PosY2 < 2912 and PosX3 < 416 and 2496 < PosY3 < 2912 and PosX4 < 416 and 2496 < PosY4 < 2912:
                                                        print("Replace? 2")
                                                        coord_X = PosX1
                                                        coord_Y = PosY1 - 2496
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "2496" and basename2 == "416":
                                print("basey == 2496 and basex == 416")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 416 < PosX1 < 832 and 2496 < PosY1 < 2912 and 416 < PosX2 < 832 and 2496 < PosY2 < 2912 and 416 < PosX3 < 832 and 2496 < PosY3 < 2912 and 416 < PosX4 < 832 and 2496 < PosY4 < 2912:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 416
                                                coord_Y = PosY1 - 2496
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 416 < PosX1 < 832 and 2496 < PosY1 < 2912 and 416 < PosX2 < 832 and 2496 < PosY2 < 2912 and 416 < PosX3 < 832 and 2496 < PosY3 < 2912 and 416 < PosX4 < 832 and 2496 < PosY4 < 2912:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 416
                                                        coord_Y = PosY1 - 2496
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "2496" and basename2 == "832":
                                print("basey == 2496 and basex == 832")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 832 < PosX1 < 1248 and 2496 < PosY1 < 2912 and 832 < PosX2 < 1248 and 2496 < PosY2 < 2912 and 832 < PosX3 < 1248 and 2496 < PosY3 < 2912 and 832 < PosX4 < 1248 and 2496 < PosY4 < 2912:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 832
                                                coord_Y = PosY1 - 2496
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 832 < PosX1 < 1248 and 2496 < PosY1 < 2912 and 832 < PosX2 < 1248 and 2496 < PosY2 < 2912 and 832 < PosX3 < 1248 and 2496 < PosY3 < 2912 and 832 < PosX4 < 1248 and 2496 < PosY4 < 2912:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 832
                                                        coord_Y = PosY1 - 2496
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")
                                        f.close()

                        elif basename1 == "2496" and basename2 == "1248":
                                print("basey == 2496 and basex == 1248")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 1248 < PosX1 < 1664 and 2496 < PosY1 < 2912 and 1248 < PosX2 < 1664 and 2496 < PosY2 < 2912 and 1248 < PosX3 < 1664 and 2496 < PosY3 < 2912 and 1248 < PosX4 < 1664 and 2496 < PosY4 < 2912:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 1248
                                                coord_Y = PosY1 - 2496
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 1248 < PosX1 < 1664 and 2496 < PosY1 < 2912 and 1248 < PosX2 < 1664 and 2496 < PosY2 < 2912 and 1248 < PosX3 < 1664 and 2496 < PosY3 < 2912 and 1248 < PosX4 < 1664 and 2496 < PosY4 < 2912:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 1248
                                                        coord_Y = PosY1 - 2496
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "2496" and basename2 == "1664":
                                print("basey == 2496 and basex == 1664")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 1664 < PosX1 < 2080 and 2496 < PosY1 < 2912 and 1664 < PosX2 < 2080 and 2496 < PosY2 < 2912 and 1664 < PosX3 < 2080 and 2496 < PosY3 < 2912 and 1664 < PosX4 < 2080 and 2496 < PosY4 < 2912:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 1664
                                                coord_Y = PosY1 - 2496
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 1664 < PosX1 < 2080 and 2496 < PosY1 < 2912 and 1664 < PosX2 < 2080 and 2496 < PosY2 < 2912 and 1664 < PosX3 < 2080 and 2496 < PosY3 < 2912 and 1664 < PosX4 < 2080 and 2496 < PosY4 < 2912:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 1664
                                                        coord_Y = PosY1 - 2496
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "2496" and basename2 == "2080":
                                print("basey == 2496 and basex == 2080")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 2080 < PosX1 < 2496 and 2496 < PosY1 < 2912 and 2080 < PosX2 < 2496 and 2496 < PosY2 < 2912 and 2080 < PosX3 < 2496 and 2496 < PosY3 < 2912 and 2080 < PosX4 < 2496 and 2496 < PosY4 < 2912:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 2080
                                                coord_Y = PosY1 - 2496
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 2080 < PosX1 < 2496 and 2496 < PosY1 < 2912 and 2080 < PosX2 < 2496 and 2496 < PosY2 < 2912 and 2080 < PosX3 < 2496 and 2496 < PosY3 < 2912 and 2080 < PosX4 < 2496 and 2496 < PosY4 < 2912:

                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 2080
                                                        coord_Y = PosY1 - 2496
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "2496" and basename2 == "2496":
                                print("basey == 2496 and basex == 2496")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 2496 < PosX1 < 2912 and 2496 < PosY1 < 2912 and 2496 < PosX2 < 2912 and 2496 < PosY2 < 2912 and 2496 < PosX3 < 2912 and 2496 < PosY3 < 2912 and 2496 < PosX4 < 2912 and 2496 < PosY4 < 2912:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 2496
                                                coord_Y = PosY1 - 2496
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 2496 < PosX1 < 2912 and 2496 < PosY1 < 2912 and 2496 < PosX2 < 2912 and 2496 < PosY2 < 2912 and 2496 < PosX3 < 2912 and 2496 < PosY3 < 2912 and 2496 < PosX4 < 2912 and 2496 < PosY4 < 2912:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 2496
                                                        coord_Y = PosY1 - 2496
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "2496" and basename2 == "2912":
                                print("basey == 2496 and basex == 2912")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 2912 < PosX1 < 3328 and 2496 < PosY1 < 2912 and 2912 < PosX2 < 3328 and 2496 < PosY2 < 2912 and 2912 < PosX3 < 3328 and 2496 < PosY3 < 2912 and 2912 < PosX4 < 3328 and 2496 < PosY4 < 2912:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 2912
                                                coord_Y = PosY1 - 2496
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 2912 < PosX1 < 3328 and 2496 < PosY1 < 2912 and 2912 < PosX2 < 3328 and 2496 < PosY2 < 2912 and 2912 < PosX3 < 3328 and 2496 < PosY3 < 2912 and 2912 < PosX4 < 3328 and 2496 < PosY4 < 2912:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 2912
                                                        coord_Y = PosY1 - 2496
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                                        #####

                        elif basename1 == "2496" and basename2 == "3328":
                                print("basey == 2496 and basex == 3328")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 3328 < PosX1 < 3744 and 2496 < PosY1 < 2912 and 3328 < PosX2 < 3744 and 2496 < PosY2 < 2912 and 3328 < PosX3 < 3744 and 2496 < PosY3 < 2912 and 3328 < PosX4 < 3744 and 2496 < PosY4 < 2912:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 3328
                                                coord_Y = PosY1 - 2496
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 3328 < PosX1 < 3744 and 2496 < PosY1 < 2912 and 3328 < PosX2 < 3744 and 2496 < PosY2 < 2912 and 3328 < PosX3 < 3744 and 2496 < PosY3 < 2912 and 3328 < PosX4 < 3744 and 2496 < PosY4 < 2912:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 3328
                                                        coord_Y = PosY1 - 2496
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "2496" and basename2 == "3744":
                                print("basey == 2496 and basex == 3744")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 3744 < PosX1 < 4160 and 2496 < PosY1 < 2912 and 3744 < PosX2 < 4160 and 2496 < PosY2 < 2912 and 3744 < PosX3 < 4160 and 2496 < PosY3 < 2912 and 3744 < PosX4 < 4160 and 2496 < PosY4 < 2912:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 3744
                                                coord_Y = PosY1 - 2496
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 3744 < PosX1 < 4160 and 2496 < PosY1 < 2912 and 3744 < PosX2 < 4160 and 2496 < PosY2 < 2912 and 3744 < PosX3 < 4160 and 2496 < PosY3 < 2912 and 3744 < PosX4 < 4160 and 2496 < PosY4 < 2912:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 3744
                                                        coord_Y = PosY1 - 2496
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        # Y = 2912

                        elif basename1 == "2912" and basename2 == "0":
                                print("basey == 2912 and basex == 0")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if PosX1 < 416 and 2912 < PosY1 < 3328 and PosX2 < 416 and 2912 < PosY2 < 3328 and PosX3 < 416 and 2912 < PosY3 < 3328 and PosX4 < 416 and 2912 < PosY4 < 3328:
                                                print("Replace? 1")
                                                coord_X = PosX1
                                                coord_Y = PosY1 - 2912
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if PosX1 < 416 and 2912 < PosY1 < 3328 and PosX2 < 416 and 2912 < PosY2 < 3328 and PosX3 < 416 and 2912 < PosY3 < 3328 and PosX4 < 416 and 2912 < PosY4 < 3328:
                                                        print("Replace? 2")
                                                        coord_X = PosX1
                                                        coord_Y = PosY1 - 2912
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "2912" and basename2 == "416":
                                print("basey == 2912 and basex == 416")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 416 < PosX1 < 832 and 2912 < PosY1 < 3328 and 416 < PosX2 < 832 and 2912 < PosY2 < 3328 and 416 < PosX3 < 832 and 2912 < PosY3 < 3328 and 416 < PosX4 < 832 and 2912 < PosY4 < 3328:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 416
                                                coord_Y = PosY1 - 2912
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 416 < PosX1 < 832 and 2912 < PosY1 < 3328 and 416 < PosX2 < 832 and 2912 < PosY2 < 3328 and 416 < PosX3 < 832 and 2912 < PosY3 < 3328 and 416 < PosX4 < 832 and 2912 < PosY4 < 3328:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 416
                                                        coord_Y = PosY1 - 2912
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "2912" and basename2 == "832":
                                print("basey == 2912 and basex == 832")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 832 < PosX1 < 1248 and 2912 < PosY1 < 3328 and 832 < PosX2 < 1248 and 2912 < PosY2 < 3328 and 832 < PosX3 < 1248 and 2912 < PosY3 < 3328 and 832 < PosX4 < 1248 and 2912 < PosY4 < 3328:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 832
                                                coord_Y = PosY1 - 2912
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 832 < PosX1 < 1248 and 2912 < PosY1 < 3328 and 832 < PosX2 < 1248 and 2912 < PosY2 < 3328 and 832 < PosX3 < 1248 and 2912 < PosY3 < 3328 and 832 < PosX4 < 1248 and 2912 < PosY4 < 3328:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 832
                                                        coord_Y = PosY1 - 2912
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "2912" and basename2 == "1248":
                                print("basey == 2912 and basex == 1248")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 1248 < PosX1 < 1664 and 2912 < PosY1 < 3328 and 1248 < PosX2 < 1664 and 2912 < PosY2 < 3328 and 1248 < PosX3 < 1664 and 2912 < PosY3 < 3328 and 1248 < PosX4 < 1664 and 2912 < PosY4 < 3328:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 1248
                                                coord_Y = PosY1 - 2912
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 1248 < PosX1 < 1664 and 2912 < PosY1 < 3328 and 1248 < PosX2 < 1664 and 2912 < PosY2 < 3328 and 1248 < PosX3 < 1664 and 2912 < PosY3 < 3328 and 1248 < PosX4 < 1664 and 2912 < PosY4 < 3328:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 1248
                                                        coord_Y = PosY1 - 2912
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "2912" and basename2 == "1664":
                                print("basey == 2912 and basex == 1664")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 1664 < PosX1 < 2080 and 2912 < PosY1 < 3328 and 1664 < PosX2 < 2080 and 2912 < PosY2 < 3328 and 1664 < PosX3 < 2080 and 2912 < PosY3 < 3328 and 1664 < PosX4 < 2080 and 2912 < PosY4 < 3328:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 1664
                                                coord_Y = PosY1 - 2912
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 1664 < PosX1 < 2080 and 2912 < PosY1 < 3328 and 1664 < PosX2 < 2080 and 2912 < PosY2 < 3328 and 1664 < PosX3 < 2080 and 2912 < PosY3 < 3328 and 1664 < PosX4 < 2080 and 2912 < PosY4 < 3328:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 1664
                                                        coord_Y = PosY1 - 2912
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "2912" and basename2 == "2080":
                                print("basey == 2912 and basex == 2080")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 2080 < PosX1 < 2496 and 2912 < PosY1 < 3328 and 2080 < PosX2 < 2496 and 2912 < PosY2 < 3328 and 2080 < PosX3 < 2496 and 2912 < PosY3 < 3328 and 2080 < PosX4 < 2496 and 2912 < PosY4 < 3328:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 2080
                                                coord_Y = PosY1 - 2912
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 2080 < PosX1 < 2496 and 2912 < PosY1 < 3328 and 2080 < PosX2 < 2496 and 2912 < PosY2 < 3328 and 2080 < PosX3 < 2496 and 2912 < PosY3 < 3328 and 2080 < PosX4 < 2496 and 2912 < PosY4 < 3328:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 2080
                                                        coord_Y = PosY1 - 2912
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "2912" and basename2 == "2496":
                                print("basey == 2912 and basex == 2496")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 2496 < PosX1 < 2912 and 2912 < PosY1 < 3328 and 2496 < PosX2 < 2912 and 2912 < PosY2 < 3328 and 2496 < PosX3 < 2912 and 2912 < PosY3 < 3328 and 2496 < PosX4 < 2912 and 2912 < PosY4 < 3328:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 2496
                                                coord_Y = PosY1 - 2912
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 2496 < PosX1 < 2912 and 2912 < PosY1 < 3328 and 2496 < PosX2 < 2912 and 2912 < PosY2 < 3328 and 2496 < PosX3 < 2912 and 2912 < PosY3 < 3328 and 2496 < PosX4 < 2912 and 2912 < PosY4 < 3328:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 2496
                                                        coord_Y = PosY1 - 2912
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "2912" and basename2 == "2912":
                                print("basey == 2912 and basex == 2912")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 2912 < PosX1 < 3328 and 2912 < PosY1 < 3328 and 2912 < PosX2 < 3328 and 2912 < PosY2 < 3328 and 2912 < PosX3 < 3328 and 2912 < PosY3 < 3328 and 2912 < PosX4 < 3328 and 2912 < PosY4 < 3328:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 2912
                                                coord_Y = PosY1 - 2912
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 2912 < PosX1 < 3328 and 2912 < PosY1 < 3328 and 2912 < PosX2 < 3328 and 2912 < PosY2 < 3328 and 2912 < PosX3 < 3328 and 2912 < PosY3 < 3328 and 2912 < PosX4 < 3328 and 2912 < PosY4 < 3328:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 2912
                                                        coord_Y = PosY1 - 2912
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "2912" and basename2 == "3328":
                                print("basey == 2912 and basex == 3328")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 3328 < PosX1 < 3744 and 2912 < PosY1 < 3328 and 3328 < PosX2 < 3744 and 2912 < PosY2 < 3328 and 3328 < PosX3 < 3744 and 2912 < PosY3 < 3328 and 3328 < PosX4 < 3744 and 2912 < PosY4 < 3328:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 3328
                                                coord_Y = PosY1 - 2912
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 3328 < PosX1 < 3744 and 2912 < PosY1 < 3328 and 3328 < PosX2 < 3744 and 2912 < PosY2 < 3328 and 3328 < PosX3 < 3744 and 2912 < PosY3 < 3328 and 3328 < PosX4 < 3744 and 2912 < PosY4 < 3328:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 3328
                                                        coord_Y = PosY1 - 2912
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "2912" and basename2 == "3744":
                                print("basey == 2912 and basex == 3744")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 3744 < PosX1 < 4160 and 2912 < PosY1 < 3328 and 3744 < PosX2 < 4160 and 2912 < PosY2 < 3328 and 3744 < PosX3 < 4160 and 2912 < PosY3 < 3328 and 3744 < PosX4 < 4160 and 2912 < PosY4 < 3328:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 3744
                                                coord_Y = PosY1 - 2912
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 3744 < PosX1 < 4160 and 2912 < PosY1 < 3328 and 3744 < PosX2 < 4160 and 2912 < PosY2 < 3328 and 3744 < PosX3 < 4160 and 2912 < PosY3 < 3328 and 3744 < PosX4 < 4160 and 2912 < PosY4 < 3328:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 3744
                                                        coord_Y = PosY1 - 2912
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        # Y = 3328

                        elif basename1 == "3328" and basename2 == "0":
                                print("basey == 3328 and basex == 0")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if PosX1 < 416 and 3328 < PosY1 < 3744 and PosX2 < 416 and 3328 < PosY2 < 3744 and PosX3 < 416 and 3328 < PosY3 < 3744 and PosX4 < 416 and 3328 < PosY4 < 3744:
                                                print("Replace? 1")
                                                coord_X = PosX1
                                                coord_Y = PosY1 - 3328
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if PosX1 < 416 and 3328 < PosY1 < 3744 and PosX2 < 416 and 3328 < PosY2 < 3744 and PosX3 < 416 and 3328 < PosY3 < 3744 and PosX4 < 416 and 3328 < PosY4 < 3744:
                                                        print("Replace? 2")
                                                        coord_X = PosX1
                                                        coord_Y = PosY1 - 3328
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "3328" and basename2 == "416":
                                print("basey == 3328 and basex == 416")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 416 < PosX1 < 832 and 3328 < PosY1 < 3744 and 416 < PosX2 < 832 and 3328 < PosY2 < 3744 and 416 < PosX3 < 832 and 3328 < PosY3 < 3744 and 416 < PosX4 < 832 and 3328 < PosY4 < 3744:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 416
                                                coord_Y = PosY1 - 3328
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 416 < PosX1 < 832 and 3328 < PosY1 < 3744 and 416 < PosX2 < 832 and 3328 < PosY2 < 3744 and 416 < PosX3 < 832 and 3328 < PosY3 < 3744 and 416 < PosX4 < 832 and 3328 < PosY4 < 3744:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 416
                                                        coord_Y = PosY1 - 3328
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "3328" and basename2 == "832":
                                print("basey == 3328 and basex == 832")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 832 < PosX1 < 1248 and 3328 < PosY1 < 3744 and 832 < PosX2 < 1248 and 3328 < PosY2 < 3744 and 832 < PosX3 < 1248 and 3328 < PosY3 < 3744 and 832 < PosX4 < 1248 and 3328 < PosY4 < 3744:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 832
                                                coord_Y = PosY1 - 3328
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 832 < PosX1 < 1248 and 3328 < PosY1 < 3744 and 832 < PosX2 < 1248 and 3328 < PosY2 < 3744 and 832 < PosX3 < 1248 and 3328 < PosY3 < 3744 and 832 < PosX4 < 1248 and 3328 < PosY4 < 3744:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 832
                                                        coord_Y = PosY1 - 3328
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                f.close()

                        elif basename1 == "3328" and basename2 == "1248":
                                print("basey == 3328 and basex == 1248")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 1248 < PosX1 < 1664 and 3328 < PosY1 < 3744 and 1248 < PosX2 < 1664 and 3328 < PosY2 < 3744 and 1248 < PosX3 < 1664 and 3328 < PosY3 < 3744 and 1248 < PosX4 < 1664 and 3328 < PosY4 < 3744:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 1248
                                                coord_Y = PosY1 - 3328
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 1248 < PosX1 < 1664 and 3328 < PosY1 < 3744 and 1248 < PosX2 < 1664 and 3328 < PosY2 < 3744 and 1248 < PosX3 < 1664 and 3328 < PosY3 < 3744 and 1248 < PosX4 < 1664 and 3328 < PosY4 < 3744:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 1248
                                                        coord_Y = PosY1 - 3328
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "3328" and basename2 == "1664":
                                print("basey == 3328 and basex == 1664")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 1664 < PosX1 < 2080 and 3328 < PosY1 < 3744 and 1664 < PosX2 < 2080 and 3328 < PosY2 < 3744 and 1664 < PosX3 < 2080 and 3328 < PosY3 < 3744 and 1664 < PosX4 < 2080 and 3328 < PosY4 < 3744:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 1664
                                                coord_Y = PosY1 - 3328
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 1664 < PosX1 < 2080 and 3328 < PosY1 < 3744 and 1664 < PosX2 < 2080 and 3328 < PosY2 < 3744 and 1664 < PosX3 < 2080 and 3328 < PosY3 < 3744 and 1664 < PosX4 < 2080 and 3328 < PosY4 < 3744:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 1664
                                                        coord_Y = PosY1 - 3328
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "3328" and basename2 == "2080":
                                print("basey == 3328 and basex == 2080")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 2080 < PosX1 < 2496 and 3328 < PosY1 < 3744 and 2080 < PosX2 < 2496 and 3328 < PosY2 < 3744 and 2080 < PosX3 < 2496 and 3328 < PosY3 < 3744 and 2080 < PosX4 < 2496 and 3328 < PosY4 < 3744:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 2080
                                                coord_Y = PosY1 - 3328
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 2080 < PosX1 < 2496 and 3328 < PosY1 < 3744 and 2080 < PosX2 < 2496 and 3328 < PosY2 < 3744 and 2080 < PosX3 < 2496 and 3328 < PosY3 < 3744 and 2080 < PosX4 < 2496 and 3328 < PosY4 < 3744:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 2080
                                                        coord_Y = PosY1 - 3328
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "3328" and basename2 == "2496":
                                print("basey == 3328 and basex == 2496")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 2496 < PosX1 < 2912 and 3328 < PosY1 < 3744 and 2496 < PosX2 < 2912 and 3328 < PosY2 < 3744 and 2496 < PosX3 < 2912 and 3328 < PosY3 < 3744 and 2496 < PosX4 < 2912 and 3328 < PosY4 < 3744:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 2496
                                                coord_Y = PosY1 - 3328
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 2496 < PosX1 < 2912 and 3328 < PosY1 < 3744 and 2496 < PosX2 < 2912 and 3328 < PosY2 < 3744 and 2496 < PosX3 < 2912 and 3328 < PosY3 < 3744 and 2496 < PosX4 < 2912 and 3328 < PosY4 < 3744:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 2496
                                                        coord_Y = PosY1 - 3328
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "3328" and basename2 == "2912":
                                print("basey == 3328 and basex == 2912")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 2912 < PosX1 < 3328 and 3328 < PosY1 < 3744 and 2912 < PosX2 < 3328 and 3328 < PosY2 < 3744 and 2912 < PosX3 < 3328 and 3328 < PosY3 < 3744 and 2912 < PosX4 < 3328 and 3328 < PosY4 < 3744:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 2912
                                                coord_Y = PosY1 - 3328
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 2912 < PosX1 < 3328 and 3328 < PosY1 < 3744 and 2912 < PosX2 < 3328 and 3328 < PosY2 < 3744 and 2912 < PosX3 < 3328 and 3328 < PosY3 < 3744 and 2912 < PosX4 < 3328 and 3328 < PosY4 < 3744:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 2912
                                                        coord_Y = PosY1 - 3328
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "3328" and basename2 == "3328":
                                print("basey == 3328 and basex == 3328")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 3328 < PosX1 < 3744 and 3328 < PosY1 < 3744 and 3328 < PosX2 < 3744 and 3328 < PosY2 < 3744 and 3328 < PosX3 < 3744 and 3328 < PosY3 < 3744 and 3328 < PosX4 < 3744 and 3328 < PosY4 < 3744:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 3328
                                                coord_Y = PosY1 - 3328
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 3328 < PosX1 < 3744 and 3328 < PosY1 < 3744 and 3328 < PosX2 < 3744 and 3328 < PosY2 < 3744 and 3328 < PosX3 < 3744 and 3328 < PosY3 < 3744 and 3328 < PosX4 < 3744 and 3328 < PosY4 < 3744:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 3328
                                                        coord_Y = PosY1 - 3328
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name,  'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name,  'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "3328" and basename2 == "3744":
                                print("basey == 3328 and basex == 3744")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 3744 < PosX1 < 4160 and 3328 < PosY1 < 3744 and 3744 < PosX2 < 4160 and 3328 < PosY2 < 3744 and 3744 < PosX3 < 4160 and 3328 < PosY3 < 3744 and 3744 < PosX4 < 4160 and 3328 < PosY4 < 3744:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 3744
                                                coord_Y = PosY1 - 3328
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 3744 < PosX1 < 4160 and 3328 < PosY1 < 3744 and 3744 < PosX2 < 4160 and 3328 < PosY2 < 3744 and 3744 < PosX3 < 4160 and 3328 < PosY3 < 3744 and 3744 < PosX4 < 4160 and 3328 < PosY4 < 3744:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 3744
                                                        coord_Y = PosY1 - 3328
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                f.close()

                        # Y = 3744

                        elif basename1 == "3744" and basename2 == "0":
                                print("basey == 3744 and basex == 0")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if PosX1 < 416 and 3744 < PosY1 < 4160 and PosX2 < 416 and 3744 < PosY2 < 4160 and PosX3 < 416 and 3744 < PosY3 < 4160 and PosX4 < 416 and 3744 < PosY4 < 4160:
                                                print("Replace? 1")
                                                coord_X = PosX1
                                                coord_Y = PosY1 - 3744
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if PosX1 < 416 and 3744 < PosY1 < 4160 and PosX2 < 416 and 3744 < PosY2 < 4160 and PosX3 < 416 and 3744 < PosY3 < 4160 and PosX4 < 416 and 3744 < PosY4 < 4160:
                                                        print("Replace? 2")
                                                        coord_X = PosX1
                                                        coord_Y = PosY1 - 3744
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "3744" and basename2 == "416":
                                print("basey == 3744 and basex == 416")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 416 < PosX1 < 832 and 3744 < PosY1 < 4160 and 416 < PosX2 < 832 and 3744 < PosY2 < 4160 and 416 < PosX3 < 832 and 3744 < PosY3 < 4160 and 416 < PosX4 < 832 and 3744 < PosY4 < 4160:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 416
                                                coord_Y = PosY1 - 3744
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 416 < PosX1 < 832 and 3744 < PosY1 < 4160 and 416 < PosX2 < 832 and 3744 < PosY2 < 4160 and 416 < PosX3 < 832 and 3744 < PosY3 < 4160 and 416 < PosX4 < 832 and 3744 < PosY4 < 4160:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 416
                                                        coord_Y = PosY1 - 3744
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "3744" and basename2 == "832":
                                print("basey == 3744 and basex == 832")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 832 < PosX1 < 1248 and 3744 < PosY1 < 4160 and 832 < PosX2 < 1248 and 3744 < PosY2 < 4160 and 832 < PosX3 < 1248 and 3744 < PosY3 < 4160 and 832 < PosX4 < 1248 and 3744 < PosY4 < 4160:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 832
                                                coord_Y = PosY1 - 3744
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 832 < PosX1 < 1248 and 3744 < PosY1 < 4160 and 832 < PosX2 < 1248 and 3744 < PosY2 < 4160 and 832 < PosX3 < 1248 and 3744 < PosY3 < 4160 and 832 < PosX4 < 1248 and 3744 < PosY4 < 4160:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 832
                                                        coord_Y = PosY1 - 3744
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "3744" and basename2 == "1248":
                                print("basey == 3744 and basex == 1248")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 1248 < PosX1 < 1664 and 3744 < PosY1 < 4160 and 1248 < PosX2 < 1664 and 3744 < PosY2 < 4160 and 1248 < PosX3 < 1664 and 3744 < PosY3 < 4160 and 1248 < PosX4 < 1664 and 3744 < PosY4 < 4160:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 1248
                                                coord_Y = PosY1 - 3744
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 1248 < PosX1 < 1664 and 3744 < PosY1 < 4160 and 1248 < PosX2 < 1664 and 3744 < PosY2 < 4160 and 1248 < PosX3 < 1664 and 3744 < PosY3 < 4160 and 1248 < PosX4 < 1664 and 3744 < PosY4 < 4160:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 1248
                                                        coord_Y = PosY1 - 3744
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "3744" and basename2 == "1664":
                                print("basey == 3744 and basex == 1664")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 1664 < PosX1 < 2080 and 3744 < PosY1 < 4160 and 1664 < PosX2 < 2080 and 3744 < PosY2 < 4160 and 1664 < PosX3 < 2080 and 3744 < PosY3 < 4160 and 1664 < PosX4 < 2080 and 3744 < PosY4 < 4160:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 1664
                                                coord_Y = PosY1 - 3744
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 1664 < PosX1 < 2080 and 3744 < PosY1 < 4160 and 1664 < PosX2 < 2080 and 3744 < PosY2 < 4160 and 1664 < PosX3 < 2080 and 3744 < PosY3 < 4160 and 1664 < PosX4 < 2080 and 3744 < PosY4 < 4160:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 1664
                                                        coord_Y = PosY1 - 3744
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "3744" and basename2 == "2080":
                                print("basey == 3744 and basex == 2080")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 2080 < PosX1 < 2496 and 3744 < PosY1 < 4160 and 2080 < PosX2 < 2496 and 3744 < PosY2 < 4160 and 2080 < PosX3 < 2496 and 3744 < PosY3 < 4160 and 2080 < PosX4 < 2496 and 3744 < PosY4 < 4160:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 2080
                                                coord_Y = PosY1 - 3744
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 2080 < PosX1 < 2496 and 3744 < PosY1 < 4160 and 2080 < PosX2 < 2496 and 3744 < PosY2 < 4160 and 2080 < PosX3 < 2496 and 3744 < PosY3 < 4160 and 2080 < PosX4 < 2496 and 3744 < PosY4 < 4160:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 2080
                                                        coord_Y = PosY1 - 3744
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "3744" and basename2 == "2496":
                                print("basey == 3744 and basex == 2496")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 2496 < PosX1 < 2912 and 3744 < PosY1 < 4160 and 2496 < PosX2 < 2912 and 3744 < PosY2 < 4160 and 2496 < PosX3 < 2912 and 3744 < PosY3 < 4160 and 2496 < PosX4 < 2912 and 3744 < PosY4 < 4160:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 2496
                                                coord_Y = PosY1 - 3744
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 2496 < PosX1 < 2912 and 3744 < PosY1 < 4160 and 2496 < PosX2 < 2912 and 3744 < PosY2 < 4160 and 2496 < PosX3 < 2912 and 3744 < PosY3 < 4160 and 2496 < PosX4 < 2912 and 3744 < PosY4 < 4160:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 2496
                                                        coord_Y = PosY1 - 3744
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "3744" and basename2 == "2912":
                                print("basey == 3744 and basex == 2912")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 2912 < PosX1 < 3328 and 3744 < PosY1 < 4160 and 2912 < PosX2 < 3328 and 3744 < PosY2 < 4160 and 2912 < PosX3 < 3328 and 3744 < PosY3 < 4160 and 2912 < PosX4 < 3328 and 3744 < PosY4 < 4160:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 2919
                                                coord_Y = PosY1 - 3744
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 2912 < PosX1 < 3328 and 3744 < PosY1 < 4160 and 2912 < PosX2 < 3328 and 3744 < PosY2 < 4160 and 2912 < PosX3 < 3328 and 3744 < PosY3 < 4160 and 2912 < PosX4 < 3328 and 3744 < PosY4 < 4160:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 2912
                                                        coord_Y = PosY1 - 3744
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "3744" and basename2 == "3328":
                                print("basey == 3744 and basex == 3328")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 3328 < PosX1 < 3744 and 3744 < PosY1 < 4160 and 3328 < PosX2 < 3744 and 3744 < PosY2 < 4160 and 3328 < PosX3 < 3744 and 3744 < PosY3 < 4160 and 3328 < PosX4 < 3744 and 3744 < PosY4 < 4160:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 3328
                                                coord_Y = PosY1 - 3744
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 3328 < PosX1 < 3744 and 3744 < PosY1 < 4160 and 3328 < PosX2 < 3744 and 3744 < PosY2 < 4160 and 3328 < PosX3 < 3744 and 3744 < PosY3 < 4160 and 3328 < PosX4 < 3744 and 3744 < PosY4 < 4160:
                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 3328
                                                        coord_Y = PosY1 - 3744
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        elif basename1 == "3744" and basename2 == "3744":
                                print("basey == 3744 and basex == 3744")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        print("Split line:")
                                        line = line.split(" ")
                                        print(line)

                                        PosX1 = int(float(line[0]))
                                        PosY1 = int(float(line[1]))
                                        PosX2 = int(float(line[2]))
                                        PosY2 = int(float(line[3]))
                                        PosX3 = int(float(line[4]))
                                        PosY3 = int(float(line[5]))
                                        PosX4 = int(float(line[6]))
                                        PosY4 = int(float(line[7]))
                                        PosClass = line[8]

                                        print(PosX1)
                                        print(PosY1)
                                        print(PosX2)
                                        print(PosY2)
                                        print(PosX3)
                                        print(PosY3)
                                        print(PosX4)
                                        print(PosY4)

                                        if 3744 < PosX1 < 4160 and 3744 < PosY1 < 4160 and 3744 < PosX2 < 4160 and 3744 < PosY2 < 4160 and 3744 < PosX3 < 4160 and 3744 < PosY3 < 4160 and 3744 < PosX4 < 4160 and 3744 < PosY4 < 4160:
                                                print("Replace? 1")
                                                coord_X = PosX1 - 3744
                                                coord_Y = PosY1 - 3744
                                                coord_H = PosX2 - PosX1
                                                coord_W = PosY4 - PosY1

                                                print("Coordenadas x, y, h, w:")
                                                print(coord_X)
                                                print(coord_Y)
                                                print(str(float(coord_H)))
                                                print(str(float(coord_W)))

                                                print("Linia replaced: ")
                                                coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))

                                                new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                print(new_list)

                                                new_line = ""

                                                for ele in new_list:
                                                        new_line += str(ele) + ","

                                                print(new_line)

                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()

                                                if not line:
                                                        continue
                                                print("Split line:")
                                                line = line.split(" ")
                                                print(line)

                                                PosX1 = int(float(line[0]))
                                                PosY1 = int(float(line[1]))
                                                PosX2 = int(float(line[2]))
                                                PosY2 = int(float(line[3]))
                                                PosX3 = int(float(line[4]))
                                                PosY3 = int(float(line[5]))
                                                PosX4 = int(float(line[6]))
                                                PosY4 = int(float(line[7]))
                                                PosClass = line[8]

                                                if 3744 < PosX1 < 4160 and 3744 < PosY1 < 4160 and 3744 < PosX2 < 4160 and 3744 < PosY2 < 4160 and 3744 < PosX3 < 4160 and 3744 < PosY3 < 4160 and 3744 < PosX4 < 4160 and 3744 < PosY4 < 4160:
                                                        print(PosX1)

                                                        print("Replace? 2")
                                                        coord_X = PosX1 - 3744
                                                        coord_Y = PosY1 - 3744
                                                        coord_H = PosX2 - PosX1
                                                        coord_W = PosY4 - PosY1

                                                        print("Coordenadas x, y, h, w:")
                                                        print(coord_X)
                                                        print(coord_Y)
                                                        print(str(float(coord_H)))
                                                        print(str(float(coord_W)))

                                                        print("Linia replaced: ")
                                                        coord_X_2 = line[0].replace(str(PosX1), str(coord_X))
                                                        print(coord_X_2)
                                                        coord_Y_2 = line[1].replace(str(PosY1), str(coord_Y))
                                                        print(coord_Y_2)

                                                        new_list = [int(float(coord_X_2)), int(float(coord_Y_2)), int(coord_H), int(coord_W), PosClass]
                                                        print(new_list)

                                                        new_line = ""

                                                        for ele in new_list:
                                                                new_line += str(ele) + ","

                                                        print(new_line)

                                                        if file_name in glob.glob('data/dataset/labels_image_merge'):

                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'w').write(new_line + "\n")

                                                        else:
                                                                filename1 = open('data/dataset/labels_image_merge/' + label_name, 'a').write(new_line + "\n")

                                        f.close()

                        # ELSE

                        else:
                                print("Error")
