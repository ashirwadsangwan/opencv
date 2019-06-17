import cv2
import numpy as np

img = cv2.imread('boxer with a toy.jpg')

cv2.line(img, (0,0), (200,200), (255,0,255), 5)
cv2.rectangle(img, (200,200), (700,700),(0, 255, 0), 5)
cv2.circle(img, (500,470), 150, (255,0,255),1)
#Drawing a polygon

points = np.array([[500,10], [20,500], [30,750], [20,750]], np.int32)
#points = points.reshape((-1, 1,2))
polygon = cv2.polylines(img, [points], True, (0,255,255), 1)

'''
True is there in the code because if it is True it connects
the first and last points. We also need to reshape it to
(1,2) form but it's already in that form so we need not
change anything.
'''

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "I'm a nice Doggo!",(380,400), font, 0.8, (0, 150, 233), 2, cv2.LINE_AA )
cv2.imshow('boxer', img)
cv2.waitKey(4000)
