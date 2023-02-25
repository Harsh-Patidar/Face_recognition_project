import numpy as np
import cv2

img = cv2.imread(r"C:\Users\91999\OneDrive\Desktop\gate\Addhar.jpeg",cv2.IMREAD_COLOR)

cv2.line(img, (0,0), (150,150), (255,255,255),10)
#we are using a line with color white so syntx for white line is (255,255,255)
# if we use (0,0,0) its black
#if we use (255,0,0) its blue
#if we use (0,255,0) its green
#if we use (0,0,255) its red
# as OpenCV work on BGR image formate
cv2.rectangle(img,(15,25),(200,150),(0,255,0) , 5)
#here we draw a rectangle of color green(0,255,0)

cv2.circle(img, (100,63), 55, (0,0,255), 2)
#if we use negative like -1 instead of 2 then circle is filled by color

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
cv2.polylines(img,[pts], True, (0,255,255), 3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV tuts!',(0,130), font, 1 , (200,255,255), 5,cv2.LINE_AA)



cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

