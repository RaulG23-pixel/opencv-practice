import cv2 as cv;

img = cv.imread('./images/imagen3.jpeg');

def rescaleFrame(frame,scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

new_img = rescaleFrame(img,0.50);
cv.imshow('Lebron', new_img);

cv.waitKey(0);


