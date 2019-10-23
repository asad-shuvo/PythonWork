import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('watch.jpg',0)
f = np.fft.fft2(img) #### Returns an array with complex value
#print(f)
fshift = np.fft.fftshift(f) ### Making the center Low frequency ..
#print(fshift[4,7])
magnitude_spectrum = 20*np.log(np.abs(fshift)) ### Taking the Magnitude

#### Showing The Images

plt.subplot(221),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'),plt.xticks([]), plt.yticks([])


#### Removing The Low Frequencis from The Frequency Domain ...
rows, cols = img.shape
crow = (int)(rows/2)
ccol = (int)(cols/2)
fshift[crow-30:crow+30, ccol-30:ccol+30] = 1 ### Applying 60x60 Mask

##Magnitude after removing the low frequency
magnitude_spectrum1 = 20*np.log(np.abs(fshift))

### Applying the reverse fourier Transform
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

plt.subplot(223),plt.imshow(magnitude_spectrum1, cmap = 'gray')
plt.title('MS after removing Low'), plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(img_back, cmap = 'gray')
plt.title('Image after HPF '), plt.xticks([]), plt.yticks([])

plt.show()
