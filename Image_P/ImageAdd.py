import cv2
import numpy as np
import matplotlib.pyplot as pyp
# img1=cv2.resize(img1,(206,320))
# img2=cv2.resize(img2,(206,320))


#Addition
#Subtraction
#Multiplication

image1=cv2.imread('3dot.jpg')
image2=cv2.imread('line.jpg')
image=np.zeros(image1.shape,image1.dtype)
image3=np.zeros(image1.shape,image1.dtype)
image4=np.zeros(image1.shape,image1.dtype)

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        image[i][j]=image1[i][j]+image2[i][j]  #For Image Addition

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        image3[i][j]=image1[i][j]-image2[i][j]  #For Image Subtraction


for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        image4[i][j]=image1[i][j]*image2[i][j]  #For Image Multiplication



pyp.figure('Arithmetic Operation of Image')
pyp.subplot(2,2,1).set_title('RGB Image')
pyp.imshow(image1)

pyp.subplot(2,2,2).set_title('After addition')  #Showing Image as ploating
pyp.imshow(image)

pyp.subplot(2,2,3).set_title('After subtraction')
pyp.imshow(image3)

pyp.subplot(2,2,4).set_title('After multiplication')
pyp.imshow(image4)

pyp.show()



arr=np.array(image1)
print(arr)
arr=np.array(image2)# Showing the pixel value
print(arr)
arr=np.array(image)
print(arr)
arr=np.array(image3)
print(arr)
arr=np.array(image4)
print(arr)
k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()