import cv2 as cv
import numpy as np

image = cv.imread('images/imagen1.jpeg')
gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY);
blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
canny = cv.Canny(blur,50,50)
blank = np.zeros(image.shape, dtype='uint8')
cv.imshow("blur",blur)

# findContours method



# Threshold method
rect, treshold = cv.threshold(gray,125,195,cv.THRESH_BINARY)
contours, hierarchies = cv.findContours(treshold,cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

print(f'{len(contours)} contours found')
cv.drawContours(blank,contours,-1,(0,255,0),1)
cv.imshow("Draw contours",blank)
#cv.imshow("Canny edges",canny);

cv.waitKey(0);