import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('watch.jpg')

mask_size = [3, 5, 7, 9, 11, 13]
x = 231

cv2.imshow('Original Image', cv2.resize(img, (256, 256)))

for n in mask_size:
    gauss = cv2.GaussianBlur(img, (n, n), 0)
    plt.subplot(x), plt.imshow(gauss), plt.title('%dx%d Gaussian Filtered' % (n, n))
    plt.xticks([]), plt.yticks([])
    x += 1

plt.show()
