import cv2
import numpy as np
import matplotlib.pyplot as pyp

ima1=cv2.imread('sea.jpg',0)
ima2=cv2.imread('Lena.jpg')

im1=255-ima1       #Negative of an image
im2=255-ima2

pyp.figure('Negative of an Image')
pyp.subplot(2,2,1).set_title('gray Image')
pyp.imshow(ima1)

pyp.subplot(2,2,2).set_title('color image')  #Showing Image as ploating
pyp.imshow(ima2)

pyp.subplot(2,2,3).set_title('Negative of gray image')
pyp.imshow(im1)

pyp.subplot(2,2,4).set_title('Negative of color image')
pyp.imshow(im2)

pyp.show()

k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
