import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

# g(x) = alpha*f(x) + beta
# g(x) - output image and f(x) - input image
# alpha - contrast
# beta - brightness
# alpha 1  beta 0      --> no change
# 0 < alpha < 1        --> lower contrast
# alpha > 1            --> higher contrast
# -127 < beta < +127   --> good range for brightness values

def modify(img):
   des = cv2.multiply(img, np.array([alpha]))
   des = cv2.add(des,beta)
   return des

def display_img(src,des):
   plt.figure('Brightness and Contrast Analysis')
   plt.subplot(221), plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
   plt.xticks([]), plt.yticks([])

   plt.subplot(222), plt.imshow(cv2.cvtColor(des, cv2.COLOR_BGR2RGB)), plt.title('Modified Brightness and Contrast')
   plt.xticks([]), plt.yticks([])

def display_hist(src,des):
   hist_src = cv2.calcHist([src],[0],None,[256],[0,256])
   hist_des = cv2.calcHist([des],[0],None,[256],[0,256])

   plt.subplot(223), plt.plot(hist_src), plt.title('Original Image Histogram')
   plt.xlim([0,256])
   plt.subplot(224), plt.plot(hist_des), plt.title('Modified Image Histogram')
   plt.xlim([0,256])

def calc_brightness(src):
   total_pixels = 0
   total_brightness = 0
   for i in range(src.shape[0]):
      for j in range(src.shape[1]):
         brightness = 0
         r,g,b = src[i][j]
         total_brightness += r*0.2126 + g * 0.7152 + b * 0.0722
         # The formula reflects the luminosity function:
         # green light contributes the most to the intensity perceived by humans,
         # and blue light the least.
         total_pixels +=1
   # print(total_pixels)
   global pixels
   pixels = total_pixels
   avg_brightness = total_brightness/total_pixels
   avg_brightness = round(avg_brightness,3)
   print('Overall brightness of the image: ',avg_brightness)
   return avg_brightness

# calculating contrast
# sqrt(1/(h*w)*(f(x)-beta)**2) - overall contrast value

def calc_contrast(src, brightness):
   arr = np.array(src)
   t = 0
   for i in range(arr.shape[0]):
      for j in range(arr.shape[1]):
         t += (arr[(i,j,0)]-brightness)**2
   sz = pixels
   contrast = t/sz
   contrast = math.sqrt(contrast)
   print('Overall Contrast: ', round(contrast,3))

def calc_standard_deviation(src, brightness):
   dif = (src - brightness)**2
   total_sum = 0
   for i in range(dif.shape[0]):
      for j in range(dif.shape[1]):
         r,g,b = dif[i][j]
         total_sum+= r + g + b

   variance = total_sum/pixels
   st_deviation = math.sqrt(variance)
   print('Standard deviation of the image: ',round(st_deviation,3))
pixels = 0
if __name__ == '__main__':
   alpha = 1.0
   beta = 0.0
   alpha = float(input('Enter alpha value [1.0-3.0]: '))
   beta = int(input('Enter beta value [-127 - 127]: '))
   src = cv2.imread('candle.jpg')
   des = modify(src)
   display_img(src,des)
   display_hist(src,des)
   brightness = calc_brightness(src)
   calc_contrast(src, brightness)
   calc_standard_deviation(src, brightness)
   plt.show()
   cv2.waitKey()
