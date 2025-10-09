# this is just a sample code file for reference on the cv2 and matplotlib usage
import cv2
from matplotlib import pyplot as plt

# Read the image (ensure the file is in the same directory)
img = cv2.imread('/path/to/image.png')

# Check if the image was loaded successfully
if img is None:
    print("Error: Image not found!")
else:
    # Convert from BGR (OpenCV default) to RGB for proper display
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Display the image using matplotlib
    plt.imshow(img_rgb)
    plt.title('RGB Image')
    plt.axis('off')  # Hide axis ticks
    plt.show()
