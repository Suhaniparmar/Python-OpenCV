import cv2
import numpy as np
# events=[i for i in dir(cv2) if 'EVENT' in i]
# print(events)

def click_event(event, x, y, flags, param):
    if event==cv2.EVENT_LBUTTONDOWN:
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,2]
        cv2.circle(img,(x,y),3,(0,98,255),-1)
        mycolor_img=np.zeros((512,512,3),np.uint8)
        mycolor_img[:]=[blue,green,red]
        cv2.imshow('color',mycolor_img)

     
#img=np.zeros((512,512,3),np.uint8)
img=cv2.imread('home.jpg')
cv2.imshow('image',img)
points=[]
cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
    