import cv2
import os
import glob
import numpy
#import numpy as np
import shutil
import random
import argparse

for filename in glob.glob('docs/DOTA29_Prueba_Labels/*.txt'):
        name, extension = os.path.splitext(os.path.basename(filename))
        #        name1 = name.split("_")
        print(name)
        # if basename ==

        with open(filename, "r") as f:
                print(filename)
                line = f.readline()
                print(line)
                if "harbor" in line:
                        print("Hay clase harbor")
                elif "bridge" in line:
                        print("Hay clase bridge")
                elif "swimming-pool" in line:
                        print("Hay clase swimming-pool")
                elif "ground-track-field" in line:
                        print("Hay clase ground-track-field")
                elif "soccer-ball-field" in line:
                        print("Hay clase soccer-ball-field")
                elif "tennis-court" in line:
                        print("Hay clase tennis-court")
                elif "basketball-court" in line:
                        print("Hay clase basketball-court")
                elif "roundabout" in line:
                        print("Hay clase roundabout")
                elif "baseball-diamond" in line:
                        print("Hay clase baseball-diamond")
                elif "storage-tank" in line:
                        print("Hay clase storage-tank")
                else:
                        print("No hay clase para eliminar")

                while line:
                        line = f.readline()
                        if "harbor" in line:
                                print("Hay clase harbor")
                        elif "bridge" in line:
                                print("Hay clase bridge")
                        elif "swimming-pool" in line:
                                print("Hay clase swimming-pool")
                        elif "ground-track-field" in line:
                                print("Hay clase ground-track-field")
                        elif "soccer-ball-field" in line:
                                print("Hay clase soccer-ball-field")
                        elif "tennis-court" in line:
                                print("Hay clase tennis-court")
                        elif "basketball-court" in line:
                                print("Hay clase basketball-court")
                        elif "roundabout" in line:
                                print("Hay clase roundabout")
                        elif "baseball-diamond" in line:
                                print("Hay clase baseball-diamond")
                        elif "storage-tank" in line:
                                print("Hay clase storage-tank")
                        else:
                                print("No hay clase para eliminar")
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

                                # print("Hola13")

#----------------------------------------------------------------------------------------------------
#parser = argparse.ArgumentParser()
#parser.add_argument("--images_num", type=int, default=1000)
#parser.add_argument("--image_size", type=int, default=416)
#parser.add_argument("--images_path", type=str, default="docs/Images/")
#parser.add_argument("--labels_txt", type=str, default="docs/DOTA29_Prueba_Labels/*.txt")
#parser.add_argument("--small", type=int, default=3)
#parser.add_argument("--medium", type=int, default=6)
#parser.add_argument("--big", type=int, default=3)
#flags = parser.parse_args()

#SIZE = flags.image_size

#if os.path.exists(flags.images_path): shutil.rmtree(flags.images_path)
#os.mkdir(flags.images_path)

#image_paths  = [os.path.join(os.path.realpath("."), "docs/Prueba" + image_name) for image_name in os.listdir("docs/Prueba")]
#image_paths += [os.path.join(os.path.realpath("."), "docs/Prueba_test"  + image_name) for image_name in os.listdir("docs/Prueba_test")]

#def compute_iou(box1, box2):
#    """xmin, ymin, xmax, ymax"""

#    A1 = (box1[2] - box1[0])*(box1[3] - box1[1])
#    A2 = (box2[2] - box2[0])*(box2[3] - box2[1])

#    xmin = max(box1[0], box2[0])
#    ymin = max(box1[1], box2[1])
#    xmax = min(box1[2], box2[2])
#    ymax = min(box1[3], box2[3])

#    if ymin >= ymax or xmin >= xmax: return 0
#    return  ((xmax-xmin) * (ymax - ymin)) / (A1 + A2)

#def make_image(data, image_path, ratio=1):

#    blank = data[0]
#    boxes = data[1]
#    label = data[2]

#    ID = image_path.split("/")[-1][0]
#    image = cv2.imread(image_path)
#    image = cv2.resize(image, (int(28*ratio), int(28*ratio)))
#    h, w, c = image.shape

#    while True:
#        xmin = np.random.randint(0, SIZE-w, 1)[0]
#        ymin = np.random.randint(0, SIZE-h, 1)[0]
#        xmax = xmin + w
#        ymax = ymin + h
#        box = [xmin, ymin, xmax, ymax]

#        iou = [compute_iou(box, b) for b in boxes]
#        if max(iou) < 0.02:
#            boxes.append(box)
#            label.append(ID)
#            break

#    for i in range(w):
#        for j in range(h):
#            x = xmin + i
#            y = ymin + j
#            blank[y][x] = image[j][i]

#    # cv2.rectangle(blank, (xmin, ymin), (xmax, ymax), [0, 0, 255], 2)
#    return blank

#with open(flags.labels_txt, "w") as wf:
#    image_num = 0
#    while image_num < flags.images_num:
#        image_path = os.path.realpath(os.path.join(flags.images_path, "%06d.jpg" %(image_num+1)))
#        annotation = image_path
#        blanks = np.ones(shape=[SIZE, SIZE, 3]) * 255
#        bboxes = [[0,0,1,1]]
#        labels = [0]
#        data = [blanks, bboxes, labels]
#        bboxes_num = 0

#        # small object
#        ratios = [0.5, 0.8]
#        N = random.randint(0, flags.small)
#        if N !=0: bboxes_num += 1
#        for _ in range(N):
#            ratio = random.choice(ratios)
#            idx = random.randint(0, 54999)
#            data[0] = make_image(data, image_paths[idx], ratio)

#        # medium object
#        ratios = [1., 1.5, 2.]
#        N = random.randint(0, flags.medium)
#        if N !=0: bboxes_num += 1
#        for _ in range(N):
#            ratio = random.choice(ratios)
#            idx = random.randint(0, 54999)
#            data[0] = make_image(data, image_paths[idx], ratio)

#        # big object
#        ratios = [3., 4.]
#        N = random.randint(0, flags.big)
#        if N !=0: bboxes_num += 1
#        for _ in range(N):
#            ratio = random.choice(ratios)
#            idx = random.randint(0, 54999)
#            data[0] = make_image(data, image_paths[idx], ratio)

#        if bboxes_num == 0: continue
#        cv2.imwrite(image_path, data[0])
#        for i in range(len(labels)):
#            if i == 0: continue
#            xmin = str(bboxes[i][0])
#            ymin = str(bboxes[i][1])
#            xmax = str(bboxes[i][2])
#            ymax = str(bboxes[i][3])
#            class_ind = str(labels[i])
#            annotation += ' ' + ','.join([xmin, ymin, xmax, ymax, str(class_ind)])
#        image_num += 1
#        print("=> %s" %annotation)
#        wf.write(annotation + "\n")