import cv2
import os
import glob
import fileinput
import numpy
#import numpy as np
import shutil
import random
import argparse

for img in glob.glob('data/dataset/train_segmented/*.png'):
        cv2.imread(img)
        img_name, img_extension = os.path.splitext(os.path.basename(img))
        name1 = img_name.split("_")
        basename = name1[0]
        basename1 = name1[1]
        basename2 = name1[2]

        print("bucle filename for")

        for filename in glob.glob('data/dataset/labels_class_convert/*.txt'):
            text_name, text_extension = os.path.splitext(os.path.basename(filename))

            if basename == text_name:
                open('data/dataset/train/', 'w').write(img)



