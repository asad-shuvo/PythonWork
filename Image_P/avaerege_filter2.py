import cv2
import numpy as np
img = cv2.imread('watch.jpg',cv2.IMREAD_GRAYSCALE)
image=cv2.resize(img,(250,250))

mask1 = np.ones((3,3),np.float32)/9
mask2 = np.ones((5,5),np.float32)/25
mask3 = np.ones((7,7),np.float32)/49
mask4 = np.ones((9,9),np.float32)/81
mask5 = np.ones((11,11),np.float32)/121

#you use -1, the result (destination) image will have the same depth as the input (source) image.
averaging1 = cv2.filter2D(image, -1, mask1)
averaging2 = cv2.filter2D(image, -1, mask2)
averaging3 = cv2.filter2D(image, -1, mask3)
averaging4 = cv2.filter2D(image, -1, mask4)
averaging5 = cv2.filter2D(image, -1, mask5)

finala=cv2.hconcat([image,averaging1,averaging2])
finalb=cv2.hconcat([averaging3,averaging4,averaging5])
final=cv2.vconcat([finala,finalb])

cv2.imshow('Averaging Filtering',final)

cv2.waitKey(0)