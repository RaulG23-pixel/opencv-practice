import cv2 as cv
import numpy as np

cap = cv.VideoCapture(1);

if not cap.isOpened():
    print("Cannot open the camera")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Can't recieve the camera stream")
        break
    gray = cv.cvtColor(frame,cv.COLOR_RGB2GRAY)
    canny = cv.Canny(frame,90,90)
    dilate = cv.dilate(canny,(7,7), iterations=1)
    cv.imshow("Camera",canny)
    if cv.waitKey(1) == ord('q'):
        break;

cap.release()
cv.destroyAllWindows()