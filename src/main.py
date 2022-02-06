import cv2
import time


def display_video_color():
    # Gets access to computers webcam
    cap = cv2.VideoCapture(0)
    set_cap_1080p(cap)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error reading frame.")
            break

        cv2.imshow("frame", frame)  # Display color frame

        # Enter q on keyboard to exit, waits 1ms in between checking keystrokes
        if cv2.waitKey(1) == ord('q'):
            break

    # Shut down camera, close gui
    cap.release()
    cv2.destroyAllWindows()


file_path = "test.avi"


# Apples webcam fps cannot be changed and differs depending on the lighting. I found
# 20fps to give the best results
def record_video_color():
    # Gets access to computers webcam
    cap = cv2.VideoCapture(0)
    set_cap_1080p(cap)

    # Get system's default resolution
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    # Creates video writer with fourcc. fourcc is a codec that gets converted to an int. It's used to compress each frame
    out = cv2.VideoWriter('test.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 20, (frame_width, frame_height))

    initial_time = time.time()
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error reading frame.")
            break

        out.write(frame)
        cv2.imshow("frame", frame)

        # Enter q on keyboard to exit, waits 1ms in between checking keystrokes
        if cv2.waitKey(1) == ord('q'):
            final_time = time.time()
            print(final_time - initial_time)
            break

    # When everything done, release the video capture and video write objects
    cap.release()
    out.release()

    # Closes all the frames
    cv2.destroyAllWindows()


def display_video_gray():
    # Gets access to computers webcam
    cap = cv2.VideoCapture(0)
    set_cap_1080p(cap)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error reading frame.")
            break

        # Black and white frame
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame_gray", gray)  # Display black and white frame

        # Enter q on keyboard to exit, waits 1ms in between checking keystrokes
        if cv2.waitKey(1) == ord('q'):
            break

    # Shut down camera, close gui
    cap.release()
    cv2.destroyAllWindows()


def set_cap_1080p(cap):
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)


def set_cap_720p(cap):
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


def set_cap_480p(cap):
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


record_video_color()
