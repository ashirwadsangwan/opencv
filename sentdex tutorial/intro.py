import cv2
import numpy
import matplotlib.pyplot as plt

img = cv2.imread('boxer.jpg', cv2.IMREAD_GRAYSCALE)

'''
Using opencv
'''
#cv2.imshow('boxer', img)
#cv2.waitKey(4000)

'''
Using matplotlib
'''
#plt.imshow(img, cmap='gray')
#plt.show()

def loadImage(image_path):
    return cv2.imread(image_path)


def grayScale(image):
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)


cv2.imshow('gray', grayScale(loadImage('boxer with a toy.jpg')))
cv2.waitKey(5000)
