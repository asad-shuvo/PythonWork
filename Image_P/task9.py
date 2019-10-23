# averaging filter with different mask size
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('watch.jpg')

mask_size = [3, 5, 7, 9, 11, 13]
x = 231

ims = cv2.resize(img, (256, 256))
cv2.imshow('Original Image', ims)

for n in mask_size:
    # mask = np.ones((n,n),np.float32)/(n*n)
    # averaging = cv2.filter2D(img,-1,mask)
    averaging = cv2.blur(img, (n, n))
    plt.subplot(x), plt.imshow(averaging), plt.title('%dx%d Averaging Filtered' % (n, n))
    plt.xticks([]), plt.yticks([])
    x += 1

plt.show()
