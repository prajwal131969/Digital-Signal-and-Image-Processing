import cv2
import numpy as np

# Load the image
image = cv2.imread(r"C:\Users\prajw\OneDrive\Documents\Pictures\Uploads\WhatsApp Image 2025-12-15 at 5.27.20 PM.jpeg")

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Apply Gaussian smoothing to reduce noise
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# Create a spatial high-pass sharpening kernel
laplacian_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
], dtype=np.float32)

# Apply high-pass filter
sharpened_image = cv2.filter2D(
    blurred_image,
    -1,
    laplacian_kernel
)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Blurred Image", blurred_image)
cv2.imshow("Sharpened Image", sharpened_image)

# Wait for key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()