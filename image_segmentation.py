import cv2
import os
import glob
import numpy

for file in glob.glob('docs/DOTA29_Prueba/*.png'):
    img = cv2.imread(file)
    height = img.shape[0]
    width = img.shape[1]

    if height > 416 and width > 416:
        #M = height // 416
        #N = width // 416
        #print(range(M))
        #print(range(M))

        for y in range(0, img.shape[0], 416):
            for x in range(0, img.shape[1], 416):
                #croppedImage = img[startRow:endRow, startCol:endCol]
                #crop_img = img[y:y + h, x:x + w]
                crop_img = img[y:y + 416, x:x + 416]
                name, extension = os.path.splitext(os.path.basename(file))
                print(name)
                print(extension)
                name1 = name + "_" + str(y)
                name2 = name1 + "_" + str(x)
                print(str(y))
                print(str(x))
                filename = name2 + extension
                print(filename)

                if os.path.isfile(filename):
                    print("File exist")
                    break
                else:
                    print("File not exist")
                    output_directory = 'docs/Prueba'
                    if img.shape[0] < 416 or img.shape[1] < 416:
                        break
                    else:
                        cv2.imwrite(os.path.join(output_directory, filename), crop_img)

                    print('Successfully saved')
    else:
        print("No 416 image") 
        print("Keep calm! Image not deleted in home") 



