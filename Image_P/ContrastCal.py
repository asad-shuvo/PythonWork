from PIL import Image,ImageEnhance
import numpy as np
import math

img=Image.open('Lena.jpg')
h,w=img.size
arr=np.array(img)
total=0
b=45
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        total+=(arr[(i,j,0)]-b)*(arr[(i,j,0)]-b)
print(total)
a=h*w
contrast=total/a
contrast=math.sqrt(contrast)
print(contrast)