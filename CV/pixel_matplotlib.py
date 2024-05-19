import cv2
import matplotlib.pyplot as plt

def show_img(image):
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)) # Convert BGR to RGB for matplotlib
    plt.axis('on')  # Hide axes   
    plt.show()

# Load image
in_image = cv2.imread("home.jpg")  # Assuming it's a JPEG image

# Check if image was loaded successfully
if in_image is not None:
    show_img(in_image)
else:
    print("Error: Failed to load the image.")