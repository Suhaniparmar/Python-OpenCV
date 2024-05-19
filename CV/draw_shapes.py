import cv2
import numpy as np
img=cv2.imread('home.jpg',1)
#img=np.zeros([512,512,3],np.uint8)  

img = cv2.line(img,(0,0),(200,200),(255,0,0),10)
img=cv2.arrowedLine(img,(0,255),(255,255),(0,255,0),8)
img=cv2.rectangle(img,(300,50),(72,300),(123,123,0),10)
img=cv2.circle(img,(400,80),50,(43,189,240),5)
font=cv2.FONT_HERSHEY_TRIPLEX
img=cv2.putText(img,'openCV',(10,400),font,4,(239,49,79),5,cv2.LINE_AA)


cv2.imshow("Frame",img)

cv2.waitKey(0)
cv2.destroyAllWindows()