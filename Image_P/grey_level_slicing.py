import cv2
import numpy as np
import matplotlib.pyplot as pyp
im=cv2.imread('watch.jpg',0)
img=cv2.resize(im,(300,300))
image1=np.zeros(img.shape,img.dtype)
image2=np.zeros(img.shape,img.dtype)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img[i][j]>160:              # With background
            image1[i][j]=255           # Set L-1 if r1<=r<=r2 else set the same pixel value
        else:
            image1[i][j]=img[i][j]

for i in range(img.shape[0]):
    for j in range(img.shape[1]):      # Without background
        if img[i][j]>160:              # Set L-1 if r1<=r<=r2 else set 0
            image2[i][j]=255
        else:
            image2[i][j]=0

final=cv2.hconcat([img,image1,image2])
cv2.imshow('Image',final)

print(img)
print(image1)
print(image2)


cv2.waitKey(0)


