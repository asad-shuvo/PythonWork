from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt

i=cv2.imread('Lena.jpg')
img1=cv2.resize(i,(200,200))
j=cv2.imread('sakib.jpg.jpg')
img2=cv2.resize(j,(200,200))
plt.figure(1)
plt.subplot(221)
plt.imshow(img1)
plt.subplot(222)
plt.imshow(img2)
plt.show()
