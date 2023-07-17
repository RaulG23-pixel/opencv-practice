import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')


#blank[200:300, 300:400] = 0,255,0
#cv.imshow('Green',blank)

#cv.rectangle(blank,(0,0),(255,255),(0,255,0),thickness=-1)


#cv.circle(blank,(blank.shape[1] // 2, blank.shape[0] // 2),30,(255,0,0),thickness=1)
#cv.imshow('circle1',blank)
#cv.circle(blank,(blank.shape[1] // 2, blank.shape[0] // 2),30,(0,0,255),thickness=-1)
#cv.line(blank,(0,0),(blank.shape[1] // 2, blank.shape[0] // 2) , (255,255,255), thickness=2)

cv.putText(blank,"hello my name is raul",(0, blank.shape[0] // 2), cv.FONT_HERSHEY_COMPLEX,1.0, (0,255,0), thickness=2)

cv.imshow('circle',blank)

cv.waitKey(0);