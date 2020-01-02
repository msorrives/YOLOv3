import cv2
import os
import glob
import fileinput
import numpy
#import numpy as np
import shutil
import random
import argparse

for img in glob.glob('docs/Prueba/*.png'):
        cv2.imread(img)
        img_name, img_extension = os.path.splitext(os.path.basename(img))
        name1 = img_name.split("_")
        basename = name1[0]
        basename1 = name1[1]
        basename2 = name1[2]

        print("bucle filename for") 

        for filename in glob.glob('docs/DOTA29_Prueba_Labels/*.txt'):
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
                                        line1 = line.split(" ")
                                        print(line1)

                                        PosX1 = int(float(line1[0]))
                                        PosX2 = int(float(line1[1]))
                                        PosY1 = int(float(line1[2]))
                                        PosY2 = int(float(line1[3]))
                                        PosH1 = int(float(line1[4]))
                                        PosH2 = int(float(line1[5]))
                                        PosW1 = int(float(line1[6]))
                                        PosW2 = int(float(line1[7]))

                                        print(PosX1)
                                        print(PosX2)
                                        print(PosY1)
                                        print(PosY2)
                                        print(PosH1)
                                        print(PosH2)
                                        print(PosW1)
                                        print(PosW2)

                                        if PosX1 < 416 and PosX2 < 416:
                                                print("Equal X fuera bucle")
                                                print(PosX1)
                                                print(PosX2)

                                                if file_name in  glob.glob('docs/Prueba_Labels'):
                                                        filename1 = open('docs/Prueba_Labels/' + label_name, 'w').write(line)
                                                else:
                                                        filename1 = open('docs/Prueba_Labels/' + label_name, 'a').write(line)

                                        if PosY1 < 416 and PosY2 < 416:
                                                print("Equal Y fuera bucle")
                                                print(PosY1)
                                                print(PosY2)

                                                if file_name in  glob.glob('docs/Prueba_Labels'):
                                                        filename1 = open('docs/Prueba_Labels/' + label_name, 'w').write(line)
                                                else:
                                                        filename1 = open('docs/Prueba_Labels/' + label_name, 'a').write(line)

                                        if PosH1 < 416 and PosH2 < 416:
                                                print("Equal H fuera bucle")
                                                print(PosH1)
                                                print(PosH2)

                                                if file_name in  glob.glob('docs/Prueba_Labels'):
                                                        filename1 = open('docs/Prueba_Labels/' + label_name, 'w').write(line)
                                                else:
                                                        filename1 = open('docs/Prueba_Labels/' + label_name, 'a').write(line)

                                        if PosW1 < 416 and PosW2 < 416:
                                                print("Equal W fuera bucle")
                                                print(PosW1)
                                                print(PosW2)

                                                if file_name in  glob.glob('docs/Prueba_Labels'):
                                                        filename1 = open('docs/Prueba_Labels/' + label_name, 'w').write(line)
                                                else:
                                                        filename1 = open('docs/Prueba_Labels/' + label_name, 'a').write(line)

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()
                                                if not line:
                                                        continue

                                                line1 = line.split(" ")
                                                print(line1)

                                                PosX1 = int(float(line1[0]))
                                                PosX2 = int(float(line1[1]))
                                                PosY1 = int(float(line1[2]))
                                                PosY2 = int(float(line1[3]))
                                                PosH1 = int(float(line1[4]))
                                                PosH2 = int(float(line1[5]))
                                                PosW1 = int(float(line1[6]))
                                                PosW2 = int(float(line1[7]))

                                                if PosX1 < 416 and PosX2 < 416:
                                                        print("Equal X")
                                                        print(PosX1)
                                                        print(PosX2)

                                                        if file_name in glob.glob('docs/Prueba_Labels'):
                                                                filename1 = open('docs/Prueba_Labels/' + label_name,'w').write(line)
                                                        else:
                                                                filename1 = open('docs/Prueba_Labels/' + label_name,'a').write(line)

                                                if PosY1 < 416 and PosY2 < 416:
                                                        print("Equal Y")
                                                        print(PosY1)
                                                        print(PosY2)

                                                        if file_name in glob.glob('docs/Prueba_Labels'):
                                                                filename1 = open('docs/Prueba_Labels/' + label_name,'w').write(line)
                                                        else:
                                                                filename1 = open('docs/Prueba_Labels/' + label_name,'a').write(line)

                                                if PosH1 < 416 and PosH2 < 416:
                                                        print("Equal H")
                                                        print(PosH1)
                                                        print(PosH2)

                                                        if file_name in glob.glob('docs/Prueba_Labels'):
                                                                filename1 = open('docs/Prueba_Labels/' + label_name,'w').write(line)
                                                        else:
                                                                filename1 = open('docs/Prueba_Labels/' + label_name,'a').write(line)

                                                if PosW1 < 416 and PosW2 < 416:
                                                        print("Equal W")
                                                        print(PosW1)
                                                        print(PosW2)

                                                        if file_name in glob.glob('docs/Prueba_Labels'):
                                                                filename1 = open('docs/Prueba_Labels/' + label_name,'w').write(line)
                                                        else:
                                                                filename1 = open('docs/Prueba_Labels/' + label_name,'a').write(line)

                                        f.close()

                        elif basename1 == "0" and basename2 == "416":
                                print("basey == 0 and basex == 416")

                                with open(filename, "r") as f:
                                        line = f.readline()
                                        print(line)
                                        line1 = line.split(" ")
                                        print(line1)

                                        PosX1 = int(float(line1[0]))
                                        PosX2 = int(float(line1[1]))
                                        PosY1 = int(float(line1[2]))
                                        PosY2 = int(float(line1[3]))
                                        PosH1 = int(float(line1[4]))
                                        PosH2 = int(float(line1[5]))
                                        PosW1 = int(float(line1[6]))
                                        PosW2 = int(float(line1[7]))

                                        print(PosX1)
                                        print(PosX2)
                                        print(PosY1)
                                        print(PosY2)
                                        print(PosH1)
                                        print(PosH2)
                                        print(PosW1)
                                        print(PosW2)

                                        if PosX1 < 416 and 416 < PosX2 < 832:
                                                print("Equal X fuera bucle")
                                                print(PosX1)
                                                print(PosX2)

                                                if file_name in  glob.glob('docs/Prueba_Labels'):
                                                        filename1 = open('docs/Prueba_Labels/' + label_name, 'w').write(line)
                                                else:
                                                        filename1 = open('docs/Prueba_Labels/' + label_name, 'a').write(line)

                                        if PosY1 < 416 and 416 < PosY2 < 832:
                                                print("Equal Y fuera bucle")
                                                print(PosY1)
                                                print(PosY2)

                                                if file_name in  glob.glob('docs/Prueba_Labels'):
                                                        filename1 = open('docs/Prueba_Labels/' + label_name, 'w').write(line)
                                                else:
                                                        filename1 = open('docs/Prueba_Labels/' + label_name, 'a').write(line)

                                        if PosH1 < 416 and 416 < PosH2 < 832:
                                                print("Equal H fuera bucle")
                                                print(PosH1)
                                                print(PosH2)

                                                if file_name in  glob.glob('docs/Prueba_Labels'):
                                                        filename1 = open('docs/Prueba_Labels/' + label_name, 'w').write(line)
                                                else:
                                                        filename1 = open('docs/Prueba_Labels/' + label_name, 'a').write(line)

                                        if PosW1 < 416 and 416 < PosW2 < 832:
                                                print("Equal W fuera bucle")
                                                print(PosW1)
                                                print(PosW2)

                                                if file_name in  glob.glob('docs/Prueba_Labels'):
                                                        filename1 = open('docs/Prueba_Labels/' + label_name, 'w').write(line)
                                                else:
                                                        filename1 = open('docs/Prueba_Labels/' + label_name, 'a').write(line)

                                        while line:
                                                print("Dentro bucle")
                                                line = f.readline()
                                                if not line:
                                                        continue

                                                line1 = line.split(" ")
                                                print(line1)

                                                PosX1 = int(float(line1[0]))
                                                PosX2 = int(float(line1[1]))
                                                PosY1 = int(float(line1[2]))
                                                PosY2 = int(float(line1[3]))
                                                PosH1 = int(float(line1[4]))
                                                PosH2 = int(float(line1[5]))
                                                PosW1 = int(float(line1[6]))
                                                PosW2 = int(float(line1[7]))

                                                if PosX1 < 416 and 416 < PosX2 < 832:
                                                        print("Equal X")
                                                        print(PosX1)
                                                        print(PosX2)

                                                        if file_name in glob.glob('docs/Prueba_Labels'):
                                                                filename1 = open('docs/Prueba_Labels/' + label_name,'w').write(line)
                                                        else:
                                                                filename1 = open('docs/Prueba_Labels/' + label_name,'a').write(line)

                                                if PosY1 < 416 and 416 < PosY2 < 832:
                                                        print("Equal Y")
                                                        print(PosY1)
                                                        print(PosY2)

                                                        if file_name in glob.glob('docs/Prueba_Labels'):
                                                                filename1 = open('docs/Prueba_Labels/' + label_name,'w').write(line)
                                                        else:
                                                                filename1 = open('docs/Prueba_Labels/' + label_name,'a').write(line)

                                                if PosH1 < 416 and 416 < PosH2 < 832:
                                                        print("Equal H")
                                                        print(PosH1)
                                                        print(PosH2)

                                                        if file_name in glob.glob('docs/Prueba_Labels'):
                                                                filename1 = open('docs/Prueba_Labels/' + label_name,'w').write(line)
                                                        else:
                                                                filename1 = open('docs/Prueba_Labels/' + label_name,'a').write(line)

                                                if PosW1 < 416 and 416 < PosW2 < 832:
                                                        print("Equal W")
                                                        print(PosW1)
                                                        print(PosW2)

                                                        if file_name in glob.glob('docs/Prueba_Labels'):
                                                                filename1 = open('docs/Prueba_Labels/' + label_name,'w').write(line)
                                                        else:
                                                                filename1 = open('docs/Prueba_Labels/' + label_name,'a').write(line)

                                        f.close()

                        elif basename1 == "0" and basename2 == "832":
                                print("basey == 0 and basex == 832")
                        elif basename1 == "0" and basename2 == "1248":
                                print("basey == 0 and basex == 1248")
                        elif basename1 == "0" and basename2 == "1664":
                                print("basey == 0 and basex == 1664")
                        elif basename1 == "0" and basename2 == "2080":
                                print("basey == 0 and basex == 2080")
                        elif basename1 == "0" and basename2 == "2496":
                                print("basey == 0 and basex == 2496")
                        elif basename1 == "0" and basename2 == "2912":
                                print("basey == 0 and basex == 2912")
                        elif basename1 == "0" and basename2 == "3328":
                                print("basey == 0 and basex == 3328")
                        elif basename1 == "0" and basename2 == "3744":
                                print("basey == 0 and basex == 3744")

                        # Y = 416

                        elif basename1 == "416" and basename2 == "0":
                                print("basey == 416 and basex == 0")
                        elif basename1 == "416" and basename2 == "416":
                                print("basey == 416 and basex == 416")
                        elif basename1 == "416" and basename2 == "832":
                                print("basey == 416 and basex == 832")
                        elif basename1 == "416" and basename2 == "1248":
                                print("basey == 416 and basex == 1248")
                        elif basename1 == "416" and basename2 == "1664":
                                print("basey == 416 and basex == 1664")
                        elif basename1 == "416" and basename2 == "2080":
                                print("basey == 416 and basex == 2080")
                        elif basename1 == "416" and basename2 == "2496":
                                print("basey == 416 and basex == 2496")
                        elif basename1 == "416" and basename2 == "2912":
                                print("basey == 416 and basex == 2912")
                        elif basename1 == "416" and basename2 == "3328":
                                print("basey == 416 and basex == 3328")
                        elif basename1 == "416" and basename2 == "3744":
                                print("basey == 416 and basex == 3744")

                        # Y = 832

                        elif basename1 == "832" and basename2 == "0":
                                print("basey == 832 and basex == 0")
                        elif basename1 == "832" and basename2 == "416":
                                print("basey == 832 and basex == 416")
                        elif basename1 == "832" and basename2 == "832":
                                print("basey == 832 and basex == 832")
                        elif basename1 == "832" and basename2 == "1248":
                                print("basey == 832 and basex == 1248")
                        elif basename1 == "832" and basename2 == "1664":
                                print("basey == 832 and basex == 1664")
                        elif basename1 == "832" and basename2 == "2080":
                                print("basey == 832 and basex == 2080")
                        elif basename1 == "832" and basename2 == "2496":
                                print("basey == 832 and basex == 2496")
                        elif basename1 == "832" and basename2 == "2912":
                                print("basey == 832 and basex == 2912")
                        elif basename1 == "832" and basename2 == "3328":
                                print("basey == 832 and basex == 3328")
                        elif basename1 == "832" and basename2 == "3744":
                                print("basey == 832 and basex == 3744")

                        # Y = 1248

                        elif basename1 == "1248" and basename2 == "0":
                                print("basey == 1248 and basex == 0")
                        elif basename1 == "1248" and basename2 == "416":
                                print("basey == 1248 and basex == 416")
                        elif basename1 == "1248" and basename2 == "832":
                                print("basey == 1248 and basex == 832")
                        elif basename1 == "1248" and basename2 == "1248":
                                print("basey == 1248 and basex == 1248")
                        elif basename1 == "1248" and basename2 == "1664":
                                print("basey == 1248 and basex == 1664")
                        elif basename1 == "1248" and basename2 == "2080":
                                print("basey == 1248 and basex == 2080")
                        elif basename1 == "1248" and basename2 == "2496":
                                print("basey == 1248 and basex == 2496")
                        elif basename1 == "1248" and basename2 == "2912":
                                print("basey == 1248 and basex == 2912")
                        elif basename1 == "1248" and basename2 == "3328":
                                print("basey == 1248 and basex == 3328")
                        elif basename1 == "1248" and basename2 == "3744":
                                print("basey == 1248 and basex == 3744")

                        # Y = 1664

                        elif basename1 == "1664" and basename2 == "0":
                                print("basey == 1664 and basex == 0")
                        elif basename1 == "1664" and basename2 == "416":
                                print("basey == 1664 and basex == 416")
                        elif basename1 == "1664" and basename2 == "832":
                                print("basey == 1664 and basex == 832")
                        elif basename1 == "1664" and basename2 == "1248":
                                print("basey == 1664 and basex == 1248")
                        elif basename1 == "1664" and basename2 == "1664":
                                print("basey == 1664 and basex == 1664")
                        elif basename1 == "1664" and basename2 == "2080":
                                print("basey == 1664 and basex == 2080")
                        elif basename1 == "1664" and basename2 == "2496":
                                print("basey == 1664 and basex == 2496")
                        elif basename1 == "1664" and basename2 == "2912":
                                print("basey == 1664 and basex == 2912")
                        elif basename1 == "1664" and basename2 == "3328":
                                print("basey == 1664 and basex == 3328")
                        elif basename1 == "1664" and basename2 == "3744":
                                print("basey == 1664 and basex == 3744")

                        # Y = 2080

                        elif basename1 == "2080" and basename2 == "0":
                                print("basey == 2080 and basex == 0")
                        elif basename1 == "2080" and basename2 == "416":
                                print("basey == 2080 and basex == 416")
                        elif basename1 == "2080" and basename2 == "832":
                                print("basey == 2080 and basex == 832")
                        elif basename1 == "2080" and basename2 == "1248":
                                print("basey == 2080 and basex == 1248")
                        elif basename1 == "2080" and basename2 == "1664":
                                print("basey == 2080 and basex == 1664")
                        elif basename1 == "2080" and basename2 == "2080":
                                print("basey == 2080 and basex == 2080")
                        elif basename1 == "2080" and basename2 == "2496":
                                print("basey == 2080 and basex == 2496")
                        elif basename1 == "2080" and basename2 == "2912":
                                print("basey == 2080 and basex == 2912")
                        elif basename1 == "2080" and basename2 == "3328":
                                print("basey == 2080 and basex == 3328")
                        elif basename1 == "2080" and basename2 == "3744":
                                print("basey == 2080 and basex == 3744")

                        # Y = 2496

                        elif basename1 == "2496" and basename2 == "0":
                                print("basey == 2496 and basex == 0")
                        elif basename1 == "2496" and basename2 == "416":
                                print("basey == 2496 and basex == 416")
                        elif basename1 == "2496" and basename2 == "832":
                                print("basey == 2496 and basex == 832")
                        elif basename1 == "2496" and basename2 == "1248":
                                print("basey == 2496 and basex == 1248")
                        elif basename1 == "2496" and basename2 == "1664":
                                print("basey == 2496 and basex == 1664")
                        elif basename1 == "2496" and basename2 == "2080":
                                print("basey == 2496 and basex == 2080")
                        elif basename1 == "2496" and basename2 == "2496":
                                print("basey == 2496 and basex == 2496")
                        elif basename1 == "2496" and basename2 == "2912":
                                print("basey == 2496 and basex == 2912")
                        elif basename1 == "2496" and basename2 == "3328":
                                print("basey == 2496 and basex == 3328")
                        elif basename1 == "2496" and basename2 == "3744":
                                print("basey == 2496 and basex == 3744")

                        # Y = 2912

                        elif basename1 == "2912" and basename2 == "0":
                                print("basey == 2912 and basex == 0")
                        elif basename1 == "2912" and basename2 == "416":
                                print("basey == 2912 and basex == 416")
                        elif basename1 == "2912" and basename2 == "832":
                                print("basey == 2912 and basex == 832")
                        elif basename1 == "2912" and basename2 == "1248":
                                print("basey == 2912 and basex == 1248")
                        elif basename1 == "2912" and basename2 == "1664":
                                print("basey == 2912 and basex == 1664")
                        elif basename1 == "2912" and basename2 == "2080":
                                print("basey == 2912 and basex == 2080")
                        elif basename1 == "2912" and basename2 == "2496":
                                print("basey == 2912 and basex == 2496")
                        elif basename1 == "2912" and basename2 == "2912":
                                print("basey == 2912 and basex == 2912")
                        elif basename1 == "2912" and basename2 == "3328":
                                print("basey == 2912 and basex == 3328")
                        elif basename1 == "2912" and basename2 == "3744":
                                print("basey == 2912 and basex == 3744")

                        # Y = 3328

                        elif basename1 == "3328" and basename2 == "0":
                                print("basey == 3328 and basex == 0")
                        elif basename1 == "3328" and basename2 == "416":
                                print("basey == 3328 and basex == 416")
                        elif basename1 == "3328" and basename2 == "832":
                                print("basey == 3328 and basex == 832")
                        elif basename1 == "3328" and basename2 == "1248":
                                print("basey == 3328 and basex == 1248")
                        elif basename1 == "3328" and basename2 == "1664":
                                print("basey == 3328 and basex == 1664")
                        elif basename1 == "3328" and basename2 == "2080":
                                print("basey == 3328 and basex == 2080")
                        elif basename1 == "3328" and basename2 == "2496":
                                print("basey == 3328 and basex == 2496")
                        elif basename1 == "3328" and basename2 == "2912":
                                print("basey == 3328 and basex == 2912")
                        elif basename1 == "3328" and basename2 == "3328":
                                print("basey == 3328 and basex == 3328")
                        elif basename1 == "3328" and basename2 == "3744":
                                print("basey == 3328 and basex == 3744")

                        # Y = 3744

                        elif basename1 == "3744" and basename2 == "0":
                                print("basey == 3744 and basex == 0")
                        elif basename1 == "3744" and basename2 == "416":
                                print("basey == 3744 and basex == 416")
                        elif basename1 == "3744" and basename2 == "832":
                                print("basey == 3744 and basex == 832")
                        elif basename1 == "3744" and basename2 == "1248":
                                print("basey == 3744 and basex == 1248")
                        elif basename1 == "3744" and basename2 == "1664":
                                print("basey == 3744 and basex == 1664")
                        elif basename1 == "3744" and basename2 == "2080":
                                print("basey == 3744 and basex == 2080")
                        elif basename1 == "3744" and basename2 == "2496":
                                print("basey == 3744 and basex == 2496")
                        elif basename1 == "3744" and basename2 == "2912":
                                print("basey == 3744 and basex == 2912")
                        elif basename1 == "3744" and basename2 == "3328":
                                print("basey == 3744 and basex == 3328")
                        elif basename1 == "3744" and basename2 == "3744":
                                print("basey == 3744 and basex == 3744")

                        # ELSE

                        else:
                                print("Error")





                        #with open(filename, "r") as f:
                        #        line = f.readline()
                        #        if "harbor" in line:
                        #                print("Hay clase harbor")
                        #                continue
                        #        elif "bridge" in line:
                        #                print("Hay clase bridge")
                        #                continue
                        #        elif "swimming-pool" in line:
                        #                print("Hay clase swimming-pool")
                        #                continue
                        #        elif "ground-track-field" in line:
                        #                print("Hay clase ground-track-field")
                        #                continue
                        #        elif "soccer-ball-field" in line:
                        #                print("Hay clase soccer-ball-field")
                        #                continue
                        #        elif "tennis-court" in line:
                        #                print("Hay clase tennis-court")
                        #                continue
                        #        elif "basketball-court" in line:
                        #                print("Hay clase basketball-court")
                        #                continue
                        #        elif "roundabout" in line:
                        #                print("Hay clase roundabout")
                        #                continue
                        #        elif "baseball-diamond" in line:
                        #                print("Hay clase baseball-diamond")
                        #                continue
                        #        elif "storage-tank" in line:
                        #                print("Hay clase storage-tank")
                        #                continue
                        #        else:
                        #                print("No hay clase para eliminar")
                        #                print(line)
                        #                line1 = line.split(" ")

                                        # if con coordenadas

                        #                print(line1[9])
                        #                line = line.replace(line1[9], ',')
                        #                filename1 = open('docs/Prueba_Labels/' + file_name, 'w')
                        #                filename1.write("/root/workspace/YOLOV3/data/dataset/test/ " + line)

                                #while line:
                                #        line = f.readline()
                                #        if not line:
                                #                continue
                                #        elif "harbor" in line:
                                #                print("Hay clase harbor")
                                #                continue
                                #        elif "bridge" in line:
                                #                print("Hay clase bridge")
                                #                continue
                                #        elif "swimming-pool" in line:
                                #                print("Hay clase swimming-pool")
                                #                continue
                                #        elif "ground-track-field" in line:
                                #                print("Hay clase ground-track-field")
                                #                continue
                                #        elif "soccer-ball-field" in line:
                                #                print("Hay clase soccer-ball-field")
                                #                continue
                                #        elif "tennis-court" in line:
                                #                print("Hay clase tennis-court")
                                #                continue
                                #        elif "basketball-court" in line:
                                #                print("Hay clase basketball-court")
                                #                continue
                                #        elif "roundabout" in line:
                                #                print("Hay clase roundabout")
                                #                continue
                                #        elif "baseball-diamond" in line:
                                #                print("Hay clase baseball-diamond")
                                #                continue
                                #        elif "storage-tank" in line:
                                #                print("Hay clase storage-tank")
                                #                continue
                                #        else:
                                #                print("No hay clase para eliminar")
                                #                print(line)
                                #                line1 = line.split(" ")
                                #                print(line1[9])
                                #                line = line.replace(line1[9], '')
                                #                line = line.replace(" ", ",")
                                #                filename1 = open('docs/Prueba_Labels/' + file_name, 'a')
                                #                filename1.write(line)