import cv2

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    cv2.imshow("frame", frame)

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()