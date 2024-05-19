import cv2
import numpy as np
# events=[i for i in dir(cv2) if 'EVENT' in i]
# print(events)

def click_event(event, x, y, flags, param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),3,(0,98,255),-1)  # -1 for fill color inside the circle
        points.append((x,y))
        if len(points)>=2:
            cv2.line(img,points[-1],points[-2],(234,123,98),5)
        cv2.imshow('image',img)


img=np.zeros((512,512,3),np.uint8)
#img=cv2.imread('home.jpg')
cv2.imshow('image',img)
points=[]
cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
    