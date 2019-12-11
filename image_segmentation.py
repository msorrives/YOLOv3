import cv2
import os
import glob

for file in glob.glob('docs/DOTA29_Prueba/*.png'):
    img = cv2.imread(file)
    x = 0
    y = 0
    h = 100
    w = 100
    crop_img = img[y:y + h, x:x + w]
    name, extension = os.path.splitext(os.path.basename(file))
    print(name)
    print(extension)
    filename = name + "_0_0" + extension
    print(filename)
    print(os.path.isfile(filename))
    if os.path.isfile(filename):
        print("File exist")
        #os.revome(filename)
        break
    else:
        print("File not exist")
        #os.chdir("docs/Prueba")
        output_directory = 'docs/Prueba'
        imcrop = cv2.imwrite(os.path.join(output_directory, filename), crop_img)
        #print(filename)
        print('Successfully saved')









#----------------------------------------------
#for filename in glob.glob('docs/DOTA29_Prueba/*.png'): #assuming gif
#    print(filename)
#    img = cv2.imread(filename)
#    os.chdir("docs/Prueba")
#    x = 0
#    y = 0
#    h = 100
#    w = 100
#    crop_img = img[y:y + h, x:x + w]
#    filename = 'savedImage.png'
#    cv2.imwrite(filename, crop_img)

#print('Successfully saved')
#----------------------------------------------
#import cv2
#import os

## Using cv2.imread() method
## to read the image
#img = cv2.imread("docs/kite.jpg")
#print("imread")

## Change the current directory
## to specified directory
#os.chdir("docs/Prueba")

#x= 0
#y= 100
#h= 1000
#w= 1000
#crop_img = img[y:y+h, x:x+w]

## Filename
#filename = 'savedImage3.jpg'


## Using cv2.imwrite() method
## Saving the image
#cv2.imwrite(filename, crop_img)
#print('Successfully saved')
#----------------------------------------------
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