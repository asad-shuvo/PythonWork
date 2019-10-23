import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('watch.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gaussian = cv2.GaussianBlur(gray,(3,3),0)

#canny
img_canny = cv2.Canny(img,100,200)

#sobel
img_sobelx = cv2.Sobel(img_gaussian,cv2.CV_8U,1,0,ksize=3)
img_sobely = cv2.Sobel(img_gaussian,cv2.CV_8U,0,1,ksize=3)
img_sobel = img_sobelx + img_sobely

#prewitt
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)


plt.subplot(331),plt.imshow(img,cmap="gray"),plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(332),plt.imshow(img_canny,cmap="gray"),plt.title('Canny')
plt.xticks([]), plt.yticks([])

plt.subplot(334),plt.imshow(img_sobelx,cmap="gray"),plt.title('Sobel X')
plt.xticks([]), plt.yticks([])

plt.subplot(335),plt.imshow(img_sobely,cmap="gray"),plt.title('Sobel Y')
plt.xticks([]), plt.yticks([])

plt.subplot(336),plt.imshow(img_sobel,cmap="gray"),plt.title('Sobel')
plt.xticks([]), plt.yticks([])

plt.subplot(337),plt.imshow(img_prewittx,cmap="gray"),plt.title('Prewitt X')
plt.xticks([]), plt.yticks([])

plt.subplot(338),plt.imshow(img_prewitty,cmap="gray"),plt.title('Prewitt Y')
plt.xticks([]), plt.yticks([])


plt.subplot(339),plt.imshow(img_prewittx + img_prewitty,cmap="gray"),plt.title('Prewitt')
plt.xticks([]), plt.yticks([])


plt.show()
