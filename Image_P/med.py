from PIL import Image
import math
import cv2
img = Image.open('sakib.jpg.jpg').convert('L')
img2=cv2.imread('sakib.jpg.jpg',0);
cv2.imshow('Gray',img2)
cv2.waitKey(0)
pix = img.load()

B  = 0

for i in range(img.size[0]):
    for j in range(img.size[1]):
        B = B+pix[i,j]

print('The Total Sum of the pixel Values : ',B)

B = B/(img.size[0]*img.size[1])

print('The Brightnes : ',B)


total = 0
#contrast=root((1/(h*w))*(f(x,y)-B)^2))
for i in range(img.size[0]):
    for j in range(img.size[1]):
        total = total+(pix[i,j] - B)*(pix[i,j] - B)

contrast = (1/(img.size[0]*img.size[1]))
contrast = contrast * total
contrast = math.sqrt(contrast)

print('Contrast of the Image = ',contrast)
