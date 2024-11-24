import cv2
import time
from emailing import send_email
import glob
import os
from threading import Thread


def clean_folder():
    print("starting clean_folder()")
    images = glob.glob('*.jpg')
    for image in images:
        os.remove(image)

"""
    To use system webcam use:
    video = cv2.VideoCapture(0)
"""
video = cv2.VideoCapture(0)
time.sleep(1)
first_frame = None
# status_list is used to detect object entry and exit
status_list = []

img_count = 0

clean_folder()
while True:
    status = 0
    check, frame = video.read()

    grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grayscale_gau = cv2.GaussianBlur(grayscale_frame, (21, 21), 0)

    if first_frame is None:
        first_frame = grayscale_gau

    delta_frame = cv2.absdiff(first_frame, grayscale_gau)
    thresh_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
    dilate_frame = cv2.dilate(thresh_frame, None, iterations=5)

    # cv2.imshow("Video", dilate_frame)
    # print(delta_frame)

    contours, check = cv2.findContours(dilate_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 6000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        if rectangle.any():
            status = 1
            cv2.imwrite(f"images/{img_count}.jpg", frame)
            img_count = img_count + 1
            all_images = glob.glob("images/*.jpg")
            img_idx = int(len(all_images) / 2)
            img_with_object = all_images[img_idx]


    status_list.append(status)
    status_list = status_list[-2:]

    if status_list[0] == 1 and status_list[1] == 0:
        email_thread = Thread(target=send_email, args=(img_with_object, ))
        email_thread.daemon = True
        clean_thread = Thread(target=clean_folder)
        clean_thread.daemon = True
        email_thread.start()

    cv2.imshow('Video', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

clean_thread.start()
video.release()
