import cv2
import numpy as np
img1 = cv2.imread(r"C:\Users\91999\OneDrive\Desktop\Face_recogination\images\3D-Matplotlib.png")
img2 = cv2.imread(r"C:\Users\91999\OneDrive\Desktop\Face_recogination\images\mainsvmimage.png")

# add = img1 + img2
add = cv2.add(img1 + img2) 
cv2.imshow('add',add)
cv2.waitKey(0)
cv2.destroyAllWindows()