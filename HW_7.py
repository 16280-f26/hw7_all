# gabor filter combined feature
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Read grayscale image
img = cv2.imread("C:\\Users\\AgVBotics\\Downloads\\leaf.png", cv2.IMREAD_GRAYSCALE)

# Step 2: Define Gabor filter parameters
ksize = 51
sigmas = [2.0, 4.0]
lambd = 10.0
gamma = 0.5
psi = 0
orientations = [0, np.pi / 4, np.pi / 2, 3 * np.pi / 4]

# Step 3: Apply Gabor filters and normalize responses
# --------------------- TBD ---------------------------------
# 3.1 Iterate (nested) over all values of sigma and orientation.
# 3.2 For each combination, compute the Gabor kernel using cv2.getGaborKernel() with the given filter parameters.
# 3.3 Apply the kernel to the image using cv2.filter2D().
# 3.4 Normalize the filtered output to the range [0, 255], then convert it to uint8 type for visualization.
# 3.5 Append the normalized output to a list of filter responses.
# 3.6 Pass the list of appended outputs to Step 4 for further processing.






# Step 4: Combine all responses (max response at each pixel)
combined = np.maximum.reduce(...)
# -------------------- TBD - END ---------------------------------

# step 5: visualize
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.subplot(1, 2, 2)
plt.imshow(combined, cmap='gray')
plt.title('Combined Gabor Feature Map (Normalized)')
plt.axis('off')
plt.show()
