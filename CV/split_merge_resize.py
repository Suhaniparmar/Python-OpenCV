import numpy as np
import cv2

img = cv2.imread('home.jpg',1)

print(img.shape)
print(img.size)
print(img.dtype)

b,g,r = cv2.split(img)
img=cv2.merge((b,g,r))

obj=img[300:360, 370:430]
img[360:420, 370:430] = obj

cv2.imshow('Frame',img)
cv2.waitKey(0)
cv2.destroyAllWindows()