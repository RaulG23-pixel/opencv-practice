import cv2 as cv
import numpy as np

cap = cv.VideoCapture(1)

fourcc = cv.VideoWriter.fourcc(*'mp4v')
out = cv.VideoWriter('videos/output.mp4',fourcc,20.0,(640,480))

while cap.isOpened():
    ret,frame = cap.read()
    if not ret:
        print("ERROR,The program couldn't connect the camera, please try again")
        break
    

    out.write(frame)

    cv.imshow("Camera",frame)
    
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
out.release()
cv.destroyAllWindows()