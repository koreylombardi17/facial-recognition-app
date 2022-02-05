import cv2


def display_video_color(refresh_rate_ms):
    # Gets access to computers webcam
    cam = cv2.VideoCapture(0)

    while True:
        ret, frame = cam.read()
        if not ret:
            print("Error reading frame.")
            break

        cv2.imshow("frame", frame)  # Display color frame

        # 1 ms between frames, enter q on keyboard to exit
        if cv2.waitKey(refresh_rate_ms) == ord('q'):
            break

    # Shut down camera, close gui
    cam.release()
    cv2.destroyAllWindows()


def display_video_gray(refresh_rate_ms):
    # Gets access to computers webcam
    cam = cv2.VideoCapture(0)

    while True:
        ret, frame = cam.read()
        if not ret:
            print("Error reading frame.")
            break

        # Black and white frame
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame_gray", gray)  # Display black and white frame

        # 1 ms between frames, enter q on keyboard to exit
        if cv2.waitKey(refresh_rate_ms) == ord('q'):
            break

    # Shut down camera, close gui
    cam.release()
    cv2.destroyAllWindows()


display_video_color(1)  # 1000 fps
display_video_gray(100)  # 10 fps
