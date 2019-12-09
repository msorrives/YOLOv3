#from core.dataset import Dataset
#trainset = Dataset('./root/datatmp/maguilera/DOTA-0_29/train/images/')
#image_path = "./docs/kite.jpg"

import cv2
import os

# Using cv2.imread() method
# to read the image
img = cv2.imread("docs/kite.jpg")

print("imread")
# Change the current directory
# to specified directory
os.chdir("docs/Prueba")

# Filename
filename = 'savedImage2.jpg'
# Using cv2.imwrite() method
# Saving the image
cv2.imwrite(filename, img)

print('Successfully saved')







#def segmentize (image_path, segment_width=200, segment_height=50):
#    # Croping Formula ==> y:h, x:w
#    idx, x_axis, x_width,  = 1, 0, segment_width
#    y_axis, y_height = 0, segment_height
#    img = cv2.imread(image_path)
#    height, width, dept = img.shape
#    print("I'm a dog!")
#    while y_axis <= height:
#        while x_axis <= width:
#            crop = img[y_axis:y_height, x_axis:x_width]
#            x_axis=x_width
#            x_width+=segment_width
#            cropped_image_path = "crop/crop%d.png" % idx
#            print("I'm a cat!")
#            cv2.imwrite(cropped_image_path, crop)
#            idx+=1
#        y_axis += segment_height
#        y_height += segment_height
#        x_axis, x_width = 0, segment_width
#    img.show()