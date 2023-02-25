# VideoCapture 2..

# isme 2-2 frame aajaye gi.......
# ek frame colorfull or second one black n white



import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


#ret stands for return
#cap stands for capture
#cvtcolor() :- stands for convert color

#imshow()   :- is used to create a GUI windows and display image using imshow() fn.

#waitKey(0) :- to hold the image window on the screen by the specified no of seconds
#              ,'0' means till the user closes it ,it will hold GUI window on the screen.
