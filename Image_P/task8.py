import numpy as np
import cv2
import matplotlib.pyplot as plt

if __name__ == '__main__':
	img = cv2.imread('watch.jpg',cv2.IMREAD_GRAYSCALE) # Read the image in greyscale
	ims = cv2.resize(img,(256,256))
	#cv2.imshow('Original Image',ims)
	eight_bit_img = seven_bit_img = six_bit_img = five_bit_img = four_bit_img = three_bit_img = two_bit_img = one_bit_img = 0
	img_bits = [eight_bit_img, seven_bit_img, six_bit_img, five_bit_img, four_bit_img, three_bit_img, two_bit_img, one_bit_img]
	val = [128, 64, 32, 16, 8, 4, 2, 1]
	# Iterate over each pixel and change pixel value to binary using np.binary_repr() and store it in a list.
	lst = []
	for i in range(img.shape[0]):
	    for j in range(img.shape[1]):
	        lst.append(np.binary_repr(img[i][j], width=8))  # width = no. of bits
	for j in range(8):
		img_bits[j] = (np.array([int(i[j]) for i in lst], dtype=np.uint8) * val[j]).reshape(img.shape[0], img.shape[1])
	plt.figure("The Image Slices")
	nm = ['Bit 7','Bit 6','Bit 5','Bit 4','Bit 3','Bit 2','Bit 1','Bit 0']
	bits = [eight_bit_img, seven_bit_img, six_bit_img, five_bit_img, four_bit_img, three_bit_img, two_bit_img, one_bit_img]

	for i in range(8):
		plt.subplot(2,4,i+1).set_title(nm[i])
		plt.imshow(img_bits[i], cmap='gray')
	plt.show()
