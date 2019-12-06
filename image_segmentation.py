import cv2
from core.dataset import Dataset
trainset = Dataset('./root/datatmp/maguilera/DOTA-0_29/train/images/')

#image_path = "./docs/kite.jpg"

def segmentize (image_path, segment_width=200, segment_height=50):
    # Croping Formula ==> y:h, x:w
    idx, x_axis, x_width,  = 1, 0, segment_width
    y_axis, y_height = 0, segment_height
    img = cv2.imread(image_path)
    height, width, dept = img.shape
    while y_axis <= height:
        while x_axis <= width:
            crop = img[y_axis:y_height, x_axis:x_width]
            x_axis=x_width
            x_width+=segment_width
            cropped_image_path = "crop/crop%d.png" % idx
            cv2.imwrite(cropped_image_path, crop)
            idx+=1
        y_axis += segment_height
        y_height += segment_height
        x_axis, x_width = 0, segment_width