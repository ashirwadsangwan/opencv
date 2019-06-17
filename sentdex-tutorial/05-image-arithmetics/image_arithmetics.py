import cv2
import numpy as np

img1 = cv2.imread('3d-Matplotlib.png')
img2 = cv2.imread('mainsvmimage.png')
img3 = cv2.imread('python logo.png')

#add = img1 + img2

add = cv2.add(img1, img2)
'''
cv2.add() adds the pixels together and makes most of the
region white as a region.
'''

weighted = cv2.addWeighted(img1, 0.3, img2, 0.7, 0)
cv2.imshow('add', add)
cv2.imshow('weighted', weighted)
cv2.waitKey(5000)
