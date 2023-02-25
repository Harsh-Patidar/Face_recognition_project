import numpy as np
import cv2

img = cv2.imread(r"C:\Users\91999\OneDrive\Desktop\Face_recogination\project\Addhar.jpegs",cv2.IMREAD_COLOR)

px = img[55 ,55]
# in this we are using the color value in the form of pixel....we are giving the location in px= img[55,55] and take output as the value of pixel at that certain point.
img[55,55] = [255,255,255]
px= img[55 ,55]
# we convert that pixel into white pixel such we are using [255,255,255]
#(ROI) Region of Interest...to separate a particular portion from the image, we have to locate the area first, then we have to copy that area from the main image to another matrix
roi = img[100:150, 100:150]

watch_face = img[37:111, 107:194]
#use the same size use calculator 111-37=74 and 194-107=87

img[0:74, 0:87]= watch_face


cv2.imshow("image", img)
cv2.waitkey(0)
cv2.destroyAllWindows()
