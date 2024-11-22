import cv2
import time

"""
    To use system webcam use:
    video = cv2.VideoCapture(0)
"""
video = cv2.VideoCapture(2)
time.sleep(1)
first_frame = None
while True:
    check, frame = video.read()

    grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grayscale_gau = cv2.GaussianBlur(grayscale_frame, (21, 21), 0)

    if first_frame is None:
        first_frame = grayscale_gau

    delta_frame = cv2.absdiff(first_frame, grayscale_gau)
    thresh_frame = cv2.threshold(delta_frame, 70, 255, cv2.THRESH_BINARY)[1]
    dilate_frame = cv2.dilate(thresh_frame, None, iterations=3)


    contours, check = cv2.findContours(dilate_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Video', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

