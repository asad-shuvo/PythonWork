import cv2
import numpy as np
import matplotlib.pyplot as pyp
img = cv2.imread('candle.jpg',cv2.IMREAD_GRAYSCALE)
image=img.copy();
height=img.shape[0]
width=img.shape[1]

laplace=(1/9)*np.array(
   [[-1,0,-1],
    [-2,7,0],
    [-1,0,-2]
  ])
for i in np.arange(1,height-1):
    for j in np.arange(1,width-1):
        sum=0
        for k in np.arange(-1,2):
            for l in np.arange(-1,2):
                a=img.item(i+k,j+l)
                p=laplace[1+k,1+l]
                sum=sum+(p*a)
        b=sum
        image.itemset((i,j),b)

pyp.figure('Laplacian Filter')
pyp.subplot(2,2,1).set_title('Orginal Image')
pyp.imshow(img,cmap="gray")

pyp.subplot(2,2,2).set_title('After Filtering')#Showing Image as ploating
pyp.imshow(image,cmap="gray")
pyp.show()
cv2.waitKey(0)
cv2.destroyAllWindows()