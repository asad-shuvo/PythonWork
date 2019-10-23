import cv2
import numpy as np
import matplotlib.pyplot as pyp

#ima1=cv2.imread('dot1.jpg',0)
img1=cv2.imread('dot2.jpg')
img2=cv2.imread('white.jpg')

img2=cv2.resize(img2,(200,200))
img1=cv2.resize(img1,(200,200))

img=img1-img2;


pyp.subplot(2,2,1).set_title('First Image')  #Showing Image as ploating
pyp.imshow(img1)

# pyp.subplot(2,2,3).set_title('Negative of gray image')
# pyp.imshow(im1)

# pyp.subplot(2,2,2).set_title('Second image')
# pyp.imshow(img2)

pyp.subplot(2,2,2).set_title('Background image')
pyp.imshow(img)
pyp.show()

k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
