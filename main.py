import numpy as np
import cv2

# Gets access to computers webcam
camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    cv2.imshow('frame', frame) # Display frame
    cv2.waitKey(1) # 1ms delay between each frame

# Shut down camera, close gui
camera.release()
cv2.destroyAllWindows()

