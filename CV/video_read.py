import cv2
cap = cv2.VideoCapture(0); 

while(True):               
    ret, frame = cap.read() 

    # gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)    # for grayscale
    # cv2.imshow('Frame',gray)

    cv2.imshow('Frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):   # Press q to close the window
        break

cap.release()
cv2.destroyAllWindows()