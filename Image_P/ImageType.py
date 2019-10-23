from PIL import Image
import matplotlib.pyplot as pyp


img = Image.open('sea.png')
#img.show()
img.save('sea.jpeg')

img1 = Image.open('sea.jpeg')

img.save('sea.tiff')

img2 = Image.open('sea.tiff')

pyp.figure('Simple Image')
pyp.subplot(2,2,1).set_title('PNG')
pyp.imshow(img)
pyp.subplot(2,2,2).set_title('JPEG')
pyp.imshow(img1)
pyp.subplot(2,2,3).set_title('TIFF')
pyp.imshow(img2)

pyp.show()
