

import cv2
import numpy
import matplotlib.pyplot as plt

img1 = cv2.imread('bulb.jpg')

img2 = 255 - img1

cv2.imshow('Original',img1)
cv2.imshow('Negative',img2)

cv2.waitKey()
