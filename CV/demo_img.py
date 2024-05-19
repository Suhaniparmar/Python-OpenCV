import cv2
img=cv2.imread('home.jpg',-1)   #flag=1(for colored img)  flag=0(grayscale img) flag=-1(img with alpha channel)
print(img)

cv2.imshow('image',img)  # image is the name of the window
k=cv2.waitKey(0)         # ASCII value of key will be store in k

if k==27 :                          # if we press ESC, this condition will be match and destroy all windows
  cv2.destroyAllWindows()
elif k==ord('s'):                   # if we press s , create a new file and store in project and destroy all windows
  cv2.imwrite('home_copy.png',img)
  cv2.destroyAllWindows()