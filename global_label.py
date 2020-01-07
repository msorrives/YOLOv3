import cv2
import os
import glob
import fileinput
import numpy
#import numpy as np
import shutil
import random
import argparse

for filename in glob.glob('docs/Prueba_Labels_Classification/*.txt'):

            line = open(filename, "r").readline()
            if not line:
                continue
            line1 = str(line)
            line2 = line1[:-1]

            file_name = "dota29_train.txt"
            print(line2)


            filename1 = open('data/dataset/' + file_name, 'a').write(line2 + "\n")


