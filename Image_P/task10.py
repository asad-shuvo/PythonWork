import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('watch.jpg')
n = int(input('Enter mask size: '))
x = 331

ims = cv2.resize(img,(256,256))
cv2.imshow('Original Image',ims)

mask = np.ones((n,n),np.float32)/(n*n)
averaging = cv2.filter2D(img,-1,mask)

for i in range(9):
    plt.subplot(x),plt.imshow(averaging),plt.title('%dx%d Averaging Filtered %d'%(n,n,i+1))
    plt.xticks([]), plt.yticks([])
    x+=1
    averaging = cv2.filter2D(averaging,-1,mask)
plt.show()
