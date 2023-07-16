import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Draw',blank);

#blank[200:300, 300:400] = 0,255,0
#cv.imshow('Green',blank)

cv.rectangle(blank,(0,0),(255,500),(0,255,0),thickness=-1)
cv.imshow('Rectangle',blank);

cv.waitKey(0);