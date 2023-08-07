import cv2 as cv
import numpy as np

image = cv.imread('images/imagen4.jpeg');
gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)
lab = cv.cvtColor(image,cv.COLOR_BGR2LAB)
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)

#cv.imshow("image",image)
#cv.imshow("gray",gray)
#cv.imshow("hsv",hsv)
#cv.imshow("lab",lab)
cv.imshow("hsv_bgr",hsv_bgr)
cv.waitKey(0);