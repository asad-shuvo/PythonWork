from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt
img=cv2.imread('Lena.jpg')
alpha = 2.2
beta =50

#g(x)=alpha.f(x)+Beta
#dst=alpha.img1+Beta.img2+Gama

result=cv2.addWeighted(img,alpha,np.zeros(img.shape, img.dtype),0,beta)
result1=cv2.addWeighted(img,alpha,np.zeros(img.shape, img.dtype),0,beta)-100

# plt.figure(1)
# plt.subplot(221)
# plt.imshow(img)
# plt.subplot(222)
# plt.imshow(result)
#
# plt.show()
cv2.imshow('Orginal Image',img)
cv2.waitKey(0)
cv2.imshow('Brighter Image',result)

cv2.waitKey(0)
cv2.imshow('Low bright',result1)
cv2.waitKey(0)
cv2.destroyAllWindows()