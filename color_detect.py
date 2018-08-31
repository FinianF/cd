import cv2 as cv

def nothing(x):
    pass

#video = cv.VideoCapture(0)

cv.namedWindow('result')

cv.createTrackbar('minr', 'result', 0, 255, nothing)
cv.createTrackbar('ming', 'result', 0, 255, nothing)
cv.createTrackbar('minb', 'result', 0, 255, nothing)

cv.createTrackbar('maxr', 'result', 0, 255, nothing)
cv.createTrackbar('maxg', 'result', 0, 255, nothing)
cv.createTrackbar('maxb', 'result', 0, 255, nothing)

while True:
    # Захват видео с вебки; ret -> Bool
    '''ret, frame = video.read()
    frameCopy = frame
    if not ret:
        print('Something wrong with your cam')'''

    frame = cv.imread("C:\\Users\\loyal\\Desktop\\hackEducationCityFINAL\\hackEducationCity\\data\\test\\images\\207.jpg")
    frameCopy = frame

    minr = cv.getTrackbarPos('minr', 'result')
    ming = cv.getTrackbarPos('ming', 'result')
    minb = cv.getTrackbarPos('minb', 'result')

    maxr = cv.getTrackbarPos('maxr', 'result')
    maxg = cv.getTrackbarPos('maxg', 'result')
    maxb = cv.getTrackbarPos('maxb', 'result')

    print((minr, ming, minb), (maxr, maxg, maxb))

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    hsv = cv.blur(hsv, (9,9))
    mask = cv.inRange(hsv, (0, 27, 202), (255, 255, 255))
    mask = cv.erode(mask, None, iterations=2)
    mask = cv.dilate(mask, None, iterations=2)
    cv.imshow('Result', mask)

    contour = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    contour = contour[1]
    if contour:
        contour = sorted(contour, key=cv.contourArea, reverse=True)
        cv.drawContours(frame, contour, 0, (255, 0, 255), 3)

        (x, y, w, h) = cv.boundingRect(contour[0])
        cv.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
        cv.imshow('Rectangle', frame)

        roImg = frameCopy[y:y+h, x:x+w]
        cv.imshow('Object', roImg)

    if cv.waitKey(1) == ord('q'):
        break

video.release()
video.destroyAllWindows()