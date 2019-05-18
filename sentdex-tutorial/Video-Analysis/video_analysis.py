import cv2
import numpy as np

cap = cv2.VideoCapture(0)

"""
'0' is here for your primary webcam. Now we'll enter into a
while loop to get the VideoCapture working.

"""

while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
