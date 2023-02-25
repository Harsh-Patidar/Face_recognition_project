import numpy as np
import cv2

#img = cv2.imread(r"C:\Users\91999\OneDrive\Desktop\Face_recogination\project\colorfull_img.webp", cv2.IMREAD_COLOR)
img = cv2.imread(r"C:\Users\91999\OneDrive\Desktop\gate\Addhar.jpeg")

cv2.line(img, (0,0) , (150,150),(255,255,255), 15)

cv2.imshow('image',img)
cv2.waitkey(0)
cv2.destroyAllWindows()
