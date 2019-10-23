import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

img1 = cv2.imread('bulb.jpg')
img2 = np.zeros(img1.shape,img1.dtype)  # Null pixel value

#For log transformation the formula is s=c*log(1+r) where c and r are constant and r is the pixel value.
#c = 255/(log(1 + max_input_pixel_value))

c = 255/(np.log(1+np.max(img1)))

for i in range(img1.shape[0]):
    for j in range(img1.shape[1]):       # s=c*log(1+image)
        img2[i][j]=c*np.log(1+img1[i][j])


plt.figure('Log Transformation')
plt.subplot(1,2,1).set_title('Orginal Image')
plt.imshow(img1)

plt.subplot(1,2,2).set_title('After Log Transformation')#Showing Image as ploating
plt.imshow(img2)
plt.show()

cv2.waitKey()
