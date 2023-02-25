import cv2
import numpy as np

img = cv2.imread(r"C:\Users\91999\OneDrive\Desktop\Face_recogination\project\img_bookpage.jpg")
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
cv2.imshow('original',img)
cv2.imshow('threshold',threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()

#make img more effective and convinent...easy to recognitise the letter

#_____2______
#simplify it further.
#-------let's grayscale the image, and then do a threshold:

grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval, threshold = cv2.threshold(grayscaled, 10, 255, cv2.THRESH_BINARY)
cv2.imshow('original',img)
cv2.imshow('threshold',threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()

#____3______
#simplify it further.
#-------NOW,we can try ___"adaptive thresholding"___, which will attempt to vary the threshold, and hopefully account for the curving pages.

th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow('original',img)
cv2.imshow('Adaptive threshold',th)
cv2.waitKey(0)
cv2.destroyAllWindows()

#____4____
#There is another version of thresholding that one can do, called ___"Otsu's threshold"___. It doesn't serve us well here, but:

retval2,threshold2 = cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('original',img)
cv2.imshow('Otsu threshold',threshold2)
cv2.waitKey(0)
cv2.destroyAllWindows()