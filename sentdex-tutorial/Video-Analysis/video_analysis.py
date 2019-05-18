import cv2
import numpy as np

cap = CV2.VideoCapture(0)

"""
'0' is here for your primary webcam. Now we'll enter into a
while loop to get the VideoCapture working.

"""

while True:
    return, frame = cap.read()
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
