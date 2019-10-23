from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt

# img=cv2.imread("Lena.jpg")
#
# cv2.imshow("RGB Image",img)
#
# grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);
# cv2.imshow("Grey Image",grey_img)
# print(grey_img.shape)


#2nd Method
img=cv2.imread("Lena.jpg")
cv2.imshow("RGB IMage",img)

cv2.waitKey(0)

img1=cv2.imread("Lena.jpg",0)

cv2.imshow("Grey Image",img1)
cv2.waitKey(0)

# Grey to Binary
ret, bw=cv2.threshold(img1,127,256,cv2.THRESH_BINARY)
cv2.imshow("binary",bw)


cv2.waitKey(0)

# i=cv2.imread('Lena.jpg')
# img5=cv2.resize(img,(200,200))

# img6=cv2.resize(img1,(200,200))
# img7=cv2.resize(bw,(200,200))

plt.figure(1)
plt.subplot(2,2,1).set_title('RGB')
plt.imshow(img)
plt.subplot(2,2,2).set_title('Grey')
plt.imshow(img1)
plt.subplot(2,2,3).set_title('Binary')
plt.imshow(bw)
plt.show()
cv2.waitKey(0)

cv2.destroyAllWindows()