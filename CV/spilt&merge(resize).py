import numpy as np
import cv2

img = cv2.imread('home.jpg', 1)

print(img.shape)
print(img.size)
print(img.dtype)

# Selecting a region from the image  
obj = img[300:360, 370:440]

# Defining the target region
target_region = img[350:410, 145:215]

# Resize the obj region to match the dimensions of the target region
obj_resized = cv2.resize(obj, (target_region.shape[1], target_region.shape[0]))

# Assigning the resized obj region to the target region
img[350:410, 145:215] = obj_resized

# Splitting channels and merging them back
b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

# Displaying the modified image
cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
