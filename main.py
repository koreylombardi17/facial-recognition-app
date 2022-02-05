import numpy as np
import cv2

# Gets access to computers webcam
camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    if not ret:
        print("Error reading frame.")
        break
    # Black and white frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame", frame)  # Display color frame
    cv2.imshow("frame_gray", gray)  # Display black and white frame

    # 1 ms between frames, enter q on keyboard to exit
    if cv2.waitKey(1) == ord('q'):
        break

# Shut down camera, close gui
camera.release()
cv2.destroyAllWindows()
