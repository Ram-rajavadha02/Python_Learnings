import cv2 as cv

#reading images
#img = cv.imread('/home/hp/Pictures/cat.jpg')
#cv.imshow('Cat', img)
#v.waitKey(0)

#reading videos
capture = cv.VideoCapture('/home/hp/Videos/Screencast from 01-16-2023 06:17:00 PM.webm')       #for webcam use 0 integer.

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()