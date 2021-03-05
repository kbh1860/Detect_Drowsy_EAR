import cv2
import sys

cap = cv2.VideoCapture(0)

if cap.isOpened() == False:
    print("Cant Open The Camera")
    sys.exit(1)

while True:
    ret, img_color = cap.read()

    if ret == False:
        print("Cant Read The Camera")
        sys.exit()
    
    cv2.imshow("Show The Camera", img_color)

    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()