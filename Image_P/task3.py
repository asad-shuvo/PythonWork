import cv2
import numpy as np
import matplotlib.pyplot as plt

def display(img1,img2):
   plt.figure('Background Elimination')
   plt.subplot(121), plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)), plt.title('With Background')
   plt.xticks([]), plt.yticks([])
   plt.subplot(122), plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)), plt.title('Without Background')
   plt.xticks([]), plt.yticks([])
   plt.show()
def modify(img1,img2):
   flag = False
   dif = cv2.subtract(img2,img1)
   #cv2.imshow('demo',d)
   return dif
if __name__== '__main__':
   img1 = cv2.imread('roseBackground.jpg',0)
   x,y = img1.shape
   img2 = np.ones((x,y,1),np.uint8)*255
   display(img1,modify(img1,img2))
   cv2.waitKey()
