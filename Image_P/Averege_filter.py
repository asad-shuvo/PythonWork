import cv2
import numpy as np
img = cv2.imread('watch.jpg',cv2.IMREAD_GRAYSCALE)

mask = np.ones((3,3),np.float32)/9
image=cv2.resize(img,(250,250))
averaging1 = cv2.filter2D(image,-1,mask) #you use -1, the result (destination) image will have the same depth as the input (source) image.
averaging2 = cv2.filter2D(averaging1,-1,mask)
averaging3= cv2.filter2D(averaging2,-1,mask)
averaging4= cv2.filter2D(averaging3,-1,mask)
averaging5= cv2.filter2D(averaging4,-1,mask)
averaging6= cv2.filter2D(averaging5,-1,mask)
averaging7= cv2.filter2D(averaging6,-1,mask)

finala=cv2.hconcat([image,averaging1,averaging2,averaging3])
finalb=cv2.hconcat([averaging4,averaging5,averaging6,averaging7])
final=cv2.vconcat([finala,finalb])

cv2.imshow('Averaging Filtering',final)

cv2.waitKey(0)