import cv2

img = cv2.imread(r"C:\Users\91999\OneDrive\Desktop\WhatsApp Image 2022-10-19 at 6.08.55 AM.jpeg" )
bng = cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("image", bng)
cv2.waitKey(0)
cv2.distroyAllWindows()
