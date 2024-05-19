import cv2
cap = cv2.VideoCapture(0); 
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # or ('X','V','I','D')
out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

while(True):               
    ret, frame = cap.read() 
    if ret==True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out.write(frame)
    # gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)    # for grayscale
    # cv2.imshow('Frame',gray)

        cv2.imshow('Frame',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):   # Press q to close the window
         break
    else:
       break

cap.release()
out.release()
cv2.destroyAllWindows()