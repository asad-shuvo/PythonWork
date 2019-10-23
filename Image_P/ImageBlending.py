import cv2
import numpy as np
import matplotlib.pyplot as pyp
im1=cv2.imread('dot2.jpg')
im2=cv2.imread('dot1.jpg')

image1=cv2.resize(im1,(250,250))
image2=cv2.resize(im2,(250,250))
image = np.zeros(image1.shape,image1.dtype);

#For blending we need the formula alpha*image1+beta*image2+gamma
alpha=.5
beta=.35
gamma=.7

for i in range(image1.shape[0]):
    for j in range(image1.shape[1]):
        image[i][j]=alpha*image1[i][j]+beta*image2[i][j]+gamma

pyp.figure('Blending Operation of Image')
pyp.subplot(2,2,1).set_title('First Image')
pyp.imshow(image1)

pyp.subplot(2,2,2).set_title('Second Image')  #Showing Image as ploating
pyp.imshow(image2)

pyp.subplot(2,2,3).set_title('After Blended')
pyp.imshow(image)

pyp.show()


k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()


