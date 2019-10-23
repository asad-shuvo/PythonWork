import cv2
import numpy as np
import matplotlib.pyplot as plt

def display(img1,img2, img3):
   plt.figure('Change Detection')
   plt.subplot(131), plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)), plt.title('First Image')
   plt.xticks([]), plt.yticks([])
   plt.subplot(132), plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)), plt.title('Changed Image')
   plt.xticks([]), plt.yticks([])
   plt.subplot(133), plt.imshow(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)), plt.title('Detected Change')
   plt.xticks([]), plt.yticks([])
   plt.show()

def modify(img1,img2,img3):
   flag = False
   dif = cv2.subtract(img1,img2)
   flag = np.any(img3)
   for i in range(img1.shape[0]):
      for j in range(img2.shape[1]):
         if img1[i,j] == img2[i,j]:
            img3[i,j] = 255
         else:
            img3[i,j] = 0
   if(flag):
      print("Change is found")
   else: print("Change not found")

if __name__== '__main__':
   img1 = cv2.imread('bulb.jpg',0)

   img2 = cv2.imread('bulb2.jpg',0)

   x,y = img1.shape
   #img3 = np.ones((x,y,1),np.uint8)*255
   img3 = np.ones(img1.shape,img1.dtype)

   modify(img1,img2,img3)

   display(img1,img2, img3)

   cv2.waitKey()
