#page:-- 5
#


import cv2
import numpy as np
import matplotlib.pyplot as plt
#
img = cv2.imread(r"C:\Users\91999\OneDrive\Desktop\Face_recogination\DL_keras&Tensor_Flow.png",cv2.IMREAD_GRAYSCALE)

#IMREAD_COLOR = 1
# IMREAD_UNCHANGED = -1

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

##plt.imshow(img, cmap='gray', interpolation='blackman')
##plt.plot([50,100,80,100],'c',linewidth=5)
##plt.show()

cv2.imwrite(r'C:\Users\91999\OneDrive\Desktop\Face_recogination\DL_keras&Tensor_Flowgray.png',img)



