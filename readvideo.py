import cv2 as cv;

video = cv.VideoCapture('./videos/video1.mp4');

def rescaleFrame(frame,scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

while True:
    isTrue, frame = video.read()
    if isTrue == True:
        frame_resized = rescaleFrame(frame,0.45)
        cv.imshow('Video',frame_resized)
        if cv.waitKey(25) & 0xFF==ord('d'):
            break
    else:
        break

video.release()
cv.destroyAllWindows()
