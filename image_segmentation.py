import cv2
import os
import glob

for file in glob.glob('docs/DOTA29_Prueba/*.png'):
    img = cv2.imread(file)
    #----- Corte 0 - 0
    x = 0
    y = 0
    h = 100
    w = 100
    crop_img1 = img[y:y + h, x:x + w]
    name, extension = os.path.splitext(os.path.basename(file))
    print(name)
    print(extension)
    filename1 = name + "_0_0" + extension
    print(filename1)
    print(os.path.isfile(filename1))
    #----- Corte 0 - 1
    x = 0
    y = 0
    h = 100
    w = 100
    crop_img2 = img[y:y + h, x:x + w]
    filename2 = name + "_0_1" + extension
    # ----- Corte 1 - 0
    x = 0
    y = 0
    h = 100
    w = 100
    crop_img3 = img[y:y + h, x:x + w]
    filename3 = name + "_1_0" + extension
    # ----- Corte 1 - 1
    x = 0
    y = 0
    h = 100
    w = 100
    crop_img4 = img[y:y + h, x:x + w]
    filename4 = name + "_1_1" + extension
    # -----
    if os.path.isfile(filename1):
        print("File exist")
        break
    elif os.path.isfile(filename2):
        print("File exist")
        break
    elif os.path.isfile(filename3):
        print("File exist")
        break
    elif os.path.isfile(filename4):
        print("File exist")
        break
    else:
        print("File not exist")
        output_directory = 'docs/Prueba'
        cv2.imwrite(os.path.join(output_directory, filename1), crop_img1)
        cv2.imwrite(os.path.join(output_directory, filename2), crop_img2)
        cv2.imwrite(os.path.join(output_directory, filename3), crop_img3)
        cv2.imwrite(os.path.join(output_directory, filename4), crop_img4)
        print('Successfully saved')







