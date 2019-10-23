import cv2
import numpy as np
import matplotlib.pyplot as pyp
img = cv2.imread('watch.jpg',cv2.IMREAD_GRAYSCALE)
image=img.copy();
height=img.shape[0]
width=img.shape[1]

gauss=(1/16)*np.array(
   [[1,2,1],
    [2,4,2],
    [1,2,1]])
for i in np.arange(1,height-1):
    for j in np.arange(1,width-1):
        sum=0
        for k in np.arange(-1,2):
            for l in np.arange(-1,2):
                a=img.item(i+k,j+l)
                p=gauss[1+k,1+l]
                sum=sum+(p*a)
        b=sum
        image.itemset((i,j),b)


image1=img.copy();
gauss1=(1/273)*np.array(
   [[1,4,7,4,1],
    [4,16,26,16,4],
    [7,26,41,26,7],
    [4,16,26,16,4],
    [1,4,7,4,1]])
for m in np.arange(2,height-2):
    for n in np.arange(2,width-2):
        sum=0
        for o in np.arange(-2,3):
            for p in np.arange(-2,3):
                x=img.item(m+o,n+p)
                y=gauss1[2+o,2+p]
                sum=sum+(x*y)
        d=sum
        image1.itemset((m,n),d)
pyp.figure('Gausian')
pyp.subplot(2,2,1).set_title('Orginal Image')
pyp.imshow(img,cmap="gray")

pyp.subplot(2,2,2).set_title('3*3 Mask')#Showing Image as ploating
pyp.imshow(image,cmap="gray")

pyp.subplot(2,2,3).set_title('5*5 Mask')#Showing Image as ploating
pyp.imshow(image1,cmap="gray")
pyp.show()
cv2.waitKey(0)
cv2.destroyAllWindows()