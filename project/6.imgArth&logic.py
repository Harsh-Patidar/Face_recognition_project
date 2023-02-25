import cv2
import numpy as np

# 500 x 250
img1 = cv2.imread(r"C:\Users\91999\OneDrive\Desktop\Face_recogination\project\img_3D-Matplotlib.png")
img2 = cv2.imread(r"C:\Users\91999\OneDrive\Desktop\Face_recogination\project\img_mainsvmimage.png")

#(155,211,79) + (50,170,200) = 205,381,279...translated to (205,255,255)

#add = cv2.add(img1,img2)----its giving an error
add = img1+img2

cv2.imshow('add',add)
cv2.waitKey(0)
cv2.destroyAllWindows()

#--------------------
#____2_____

#we can add images, and have each carry a different "weight"

img1 = cv2.imread(r"C:\Users\91999\OneDrive\Desktop\Face_recogination\project\img_3D-Matplotlib.png")
img2 = cv2.imread(r"C:\Users\91999\OneDrive\Desktop\Face_recogination\project\img_mainsvmimage.png")

weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
cv2.imshow('weighted',weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()

#^^For the addWeighted method, the parameters are the first image, the weight, the second image, that weight, and then finally gamma, which is a measurement of light. We'll leave that at zero for now.

#--------------------------
#__3__


# Load two images
img1 = cv2.imread(r"C:\Users\91999\OneDrive\Desktop\Face_recogination\project\img_3D-Matplotlib.png")
img2 = cv2.imread(r"C:\Users\91999\OneDrive\Desktop\Face_recogination\project\img_mainlogo.png")

# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]

# Now create a mask of logo and create its inverse mask
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

# add a threshold__threshold is the simplest method of image segmentation
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst

cv2.imshow('res',img1)

#for debugging for our convinent we can print every single line...
cv2.imshow('mask_inv',mask_inv)
cv2.imshow('img1_bg',img1_bg)
cv2.imshow('img2_fg',img2_fg)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
