# unit 2----by:---{sentdex}
# Loading video source OpenCV with python for image and video analysis 2.

import cv2
import numpy as np

#if you use ZERO '0' then it is your first webcam (zero per isliye chal rha hai...kyo ki mera PC ka first camera hai so we use '0')
#if you use ONE '1' then it is your second webcam ( if there is another webcam then we can use '1' )

cap= cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('frame',frame)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()

# next image open at a particular time such that it will not close as the programm
#     execution as you don't stop the programm execution

