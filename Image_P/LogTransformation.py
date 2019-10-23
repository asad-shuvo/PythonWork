import cv2
import numpy as np
import math
import matplotlib.pyplot as pyp

im=cv2.imread('3dot.jpg',0)
image=cv2.resize(im, (300, 300))
img = np.zeros(image.shape,image.dtype);  # Null pixel value

c=1

for i in range(image.shape[0]):
    for j in range(image.shape[1]):       # s=c*log(1+image)
        img[i][j]=np.log(1+image[i][j])

pyp.figure('Log Transformation')
pyp.subplot(2,2,1).set_title('Orginal Image')
pyp.imshow(image)

pyp.subplot(2,2,2).set_title('After Compression')#Showing Image as ploating
pyp.imshow(img)
pyp.show()


k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
