import cv2 as cv

image = cv.imread("./images/imagen1.jpeg");
#cv.imshow("image",image);

#grayscale
gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY);
#cv.imshow("gray",gray);

#Blur
blur = cv.GaussianBlur(image,(3,3),cv.BORDER_DEFAULT);
cv.imshow("blur",blur);

#canny edges
canny = cv.Canny(blur,125,175);
cv.imshow("Canny", canny)

#dilate borders
dilated = cv.dilate(canny,(3,3),iterations=1)
cv.imshow("Dilated",dilated)



cv.waitKey(0);