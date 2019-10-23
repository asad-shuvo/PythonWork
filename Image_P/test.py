import cv2
# Image Read
img = cv2.imread('lena.jpg.png')
# Image show
cv2.imshow('Output Image',img)
# Image write
cv2.imwrite('Lena.jpg',img);
cv2.imwrite('Lena.png',img);

# Image details
print(img.shape)

print("Image Height :",img.shape[0]);
print("Image wight :",img.shape[1]);
print("Image Layers :",img.shape[2]);


# Co-ordinate BGR value
px=img[100,100]
print(px)

# Only B or G or R value. B=0,G=1,R=2
px1=img[100,100,0]
print(px1)

print(img.dtype)
print(img.size)
cv2.waitKey(0)


cv2.destroyAllWindows()