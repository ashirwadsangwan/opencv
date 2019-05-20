import cv2
import numpy as np

img = cv2.imread('boxer.jpg')

img[70, 70] = [255, 255, 255] # to put a white spot
px = img[70, 70]

img[100:150, 100:150] = [255, 255, 255]

portion = img[500:530, 600:630]

img[0:30, 0:30] = portion

cv2.imshow('portion', img)
cv2.waitKey(5000)
