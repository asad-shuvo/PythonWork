import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('bulb.jpg',0)

img1 = np.zeros(img.shape,img.dtype)
img2 = np.zeros(img.shape,img.dtype)

r1 = int(input('Enter lower range (0-255): '))
r2 = int(input('Enter upper range (0-255): '))

if r1>r2:
	r1,r2 = r2,r1

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img[i][j] >= r1 and img[i][j] <= r2:
            img1[i][j]=255
            img2[i][j]=255
        else:
            img1[i][j] = img[i][j]      # With background, Set L-1 if r1<=r<=r2 else set the same pixel value
            img2[i][j] = 0            # Without background, Set L-1 if r1<=r<=r2 else set 0


plt.figure('Gray Level Slicing')
plt.subplot(1,3,1).set_title('Orginal Image')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.subplot(1,3,2).set_title('With Background')#Showing Image as ploating
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))

plt.subplot(1,3,3).set_title('Without Background')#Showing Image as ploating
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))

plt.show()

cv2.waitKey()
