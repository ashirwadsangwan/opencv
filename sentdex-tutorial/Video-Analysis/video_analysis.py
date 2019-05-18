import cv2
import numpy as np

cap = cv2.VideoCapture(0)
"""
You can add a video path instead of "0" in the VideoCapture
if you want to process an existing video file.
"""

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (720, 560))

"""
'0' is here for your primary webcam. Now we'll enter into a
while loop to get the VideoCapture working.

"""

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    out.write(gray)
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
