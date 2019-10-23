import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('watch.jpg',cv2.IMREAD_GRAYSCALE)
mask = np.ones((5,5),np.float32)/25

plt.subplot(331),plt.imshow(img,cmap="gray"),plt.title('Original')
plt.xticks([]), plt.yticks([])

one = cv2.GaussianBlur(img,(5,5),0)
plt.subplot(332),plt.imshow(one,cmap="gray"),plt.title('One Time')
plt.xticks([]), plt.yticks([])

two = cv2.GaussianBlur(one,(5,5),0)
plt.subplot(333),plt.imshow(two,cmap="gray"),plt.title('Two Times')
plt.xticks([]), plt.yticks([])

three = cv2.GaussianBlur(two,(5,5),0)
plt.subplot(334),plt.imshow(three,cmap="gray"),plt.title('Three Times')
plt.xticks([]), plt.yticks([])

four = cv2.GaussianBlur(three,(5,5),0)
plt.subplot(335),plt.imshow(four,cmap="gray"),plt.title('Four Times')
plt.xticks([]), plt.yticks([])

five = cv2.GaussianBlur(four,(5,5),0)
plt.subplot(336),plt.imshow(five,cmap="gray"),plt.title('Five Times')
plt.xticks([]), plt.yticks([])

six = cv2.GaussianBlur(five,(5,5),0)
plt.subplot(337),plt.imshow(six,cmap="gray"),plt.title('Six Times')
plt.xticks([]), plt.yticks([])

seven = cv2.GaussianBlur(six,(5,5),0)
plt.subplot(338),plt.imshow(seven,cmap="gray"),plt.title('Seven Times')
plt.xticks([]), plt.yticks([])

eight = cv2.GaussianBlur(seven,(5,5),0)
plt.subplot(339),plt.imshow(eight,cmap="gray"),plt.title('Eight Times')
plt.xticks([]), plt.yticks([])

plt.show()