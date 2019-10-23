import cv2
import numpy as np
import matplotlib.pyplot as pyp

im = cv2.imread('dot2.jpg')
image = cv2.resize(im, (200, 200))
img = np.zeros(image.shape,image.dtype);
img1 = np.zeros(image.shape,image.dtype);  # Null pixel value
img2 = np.zeros(image.shape,image.dtype);

# For Power Law transform we know that s=cr^gamma
# where c and r is constant
c = 1
gamma=1
#img = c * np.uint8(image) ** 1  # gamma=1 then the image will be linear..Output will be same as the input
for i in range(image.shape[0]):    
    for j in range(image.shape[1]):
        img[i][j]=c*image[i][j]**gamma
gamma=.8
for i in range(image.shape[0]):     #gamma<1: a narrow range of dark or low intensity pixel values in the input image get mapped
    for j in range(image.shape[1]):
        img1[i][j]=c*image[i][j]**gamma

#gamma>1: a range of bright or high intensity pixel values in the input image get mapped
gamma=1.1
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        img2[i][j]=c*image[i][j]**gamma
# cv2.imshow('Gamma',img2)
# cv2.waitKey(0)
pyp.figure('Power Law Transformation')
pyp.subplot(2,2,1).set_title('Orginal Image')
pyp.imshow(image)

pyp.subplot(2,2,2).set_title('Gamma=1')  #Showing Image as ploating
pyp.imshow(img)

pyp.subplot(2,2,3).set_title('Gamma=.5')
pyp.imshow(img1)

pyp.subplot(2,2,4).set_title('Gamma=1.1')
pyp.imshow(img2)

pyp.show()

k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
