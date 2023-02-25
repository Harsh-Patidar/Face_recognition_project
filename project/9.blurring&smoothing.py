#We can use various blurring and smoothing techniques
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #hsv hue sat value
    lower_red = np.array([150,150,50])
    upper_red = np.array([255,255,180])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    # cv2.imshow('frame',frame)

    kernel = np.ones((15,15), np.float32)/255
    smoothed = cv2.bitwise_and(frame, frame, mask = mask)

    #blur = cv2.GaussianBlur(res, (15,15), 0)
    #median =cv2.medianBlur(res,15)
    #bilaternal = c2.bilateralFilter(res, 15 , 75 ,75)
    
    #smoothed = cv2.filter2D(res, -1, kernel)

    #blur = cv2.GaussianBlur(res, (15,15), 0)


    #cv2.imshow('mask', mask)

    cv2.imshow('frame',frame)
    #cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    #cv2.imshow('smoothed', smoothed)
    # cv2.imshow('blur', blur)
    cv2.imshow('median', median)
    # cv2.imshow('bilaternal', bilateral)



    ## cv2.imshow('mask',mask)
    ## cv2.imshow('res',res)

    k = cv2.waitKey(5) & 0xFF
    if k == 10:
        break
    

 # apply a simple smoothing, where we do a sort of averaging per block of pixels. In our case, let's do a 15 x 15 square, which means we have 225 total pixels.

#___2___

    # kernel = np.ones((15,15),np.float32)/225
    # smoothed = cv2.filter2D(res,-1,kernel)
    # cv2.imshow('Original',frame)
    # cv2.imshow('Averaging',smoothed)

    # k = cv2.waitKey(5) & 0xFF
    # if k == 27:
    #     break

cv2.destroyAllWindows()
cap.release()