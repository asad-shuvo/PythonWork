import numpy as np
import cv2
import matplotlib.pyplot as plt


def info(img):
    print("Original")
    print('Image size:', img.size)
    print('Image shape:', img.shape)
    print('Image type:', img.dtype)


def display(imgs):
    plt.figure('Basic Image Formats')
    titles = ['JPG', 'PNG', 'TIF', 'Grayscale', 'Binary']

    for i in range(5):
        plt.subplot(2, 3, i + 1), plt.imshow(cv2.cvtColor(imgs[i], cv2.COLOR_BGR2RGB)), plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()


def binaryImage(img):
    gre = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bina = np.zeros(gre.shape, gre.dtype)
    for i in range(gre.shape[0]):
        for j in range(gre.shape[1]):
            if gre[i, j] > 127:
                bina[i, j] = 255
            else:
                bina[i, j] = 0
    return bina


if __name__ == '__main__':
    img = cv2.imread('sea.jpeg')

    info(img)

    cv2.imwrite('sea_png.png', img)
    cv2.imwrite('sea_tif.tif', img)

    png = cv2.imread('sea_png.png')
    tif = cv2.imread('sea_tif.tif')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    binary = binaryImage(img)

    imgs = [img, png, tif, gray, binary]

    display(imgs)

