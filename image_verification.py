import cv2
import os
import glob
import fileinput
import numpy
#import numpy as np
import shutil
import random
import argparse

for img in glob.glob('data/dataset/train_segmented/*.jpg'):
        cv2.imread(img)
        img_name, img_extension = os.path.splitext(os.path.basename(img))

        print("bucle 1")

        for filename in glob.glob('data/dataset/labels_classification/*.txt'):
            text_name, text_extension = os.path.splitext(os.path.basename(filename))
            print("bucle 2")

            if img_name == text_name:
                #output_directory = 'data/dataset/train/'
                output_directory = 'data/dataset/test/'
                shutil.copy(img, output_directory)



