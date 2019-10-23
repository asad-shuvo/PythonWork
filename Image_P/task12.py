import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('watch.jpg')
n = int(input('Enter mask size: '))
x = 331

cv2.imshow('Original Image',cv2.resize(img,(256,256)))

gauss = cv2.GaussianBlur(img,(n,n),0)

for i in range(9):
    plt.subplot(x),plt.imshow(gauss),plt.title('%dx%d Gaussian Filtered'%(n,n))
    plt.xticks([]), plt.yticks([])
    gauss = cv2.GaussianBlur(gauss,(n,n),0)
    x+=1
plt.show()
