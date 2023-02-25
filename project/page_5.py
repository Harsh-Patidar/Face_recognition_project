import cv2
# 
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\91999\OneDrive\Desktop\Face_recogination\Screenshot 2022-10-16 012629.png",cv2.IMREAD_GRAYSCALE)
plt.imshow(img,cmap = 'gray', interpolation = 'bicubic')
plt.plot([50,100,80,100],'c',linewidth = 5)
plt.show()
