
from imutils import paths
import cv2

imagePaths = list(paths.list_images("C:\\Users\\Suhani\\Desktop\\Python\\CV\\img"))
for img in imagePaths:
     image = cv2.imread(img)
     cv2.imshow("Frame",image)
     cv2.waitKey()
cv2.destroyAllWindows()
