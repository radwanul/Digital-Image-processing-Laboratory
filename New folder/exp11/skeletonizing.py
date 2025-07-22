import cv2
import numpy as np

# Load image in grayscale
img = cv2.imread(r'D:\Academic\Fourth year Second semester\4206\Code\exp11\Thumb.png', 0)

if img is None:
    print("Image not found.")
    exit()

# Convert to binary image
_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Create empty skeleton image
skeleton = np.zeros_like(binary)

# Get structuring element
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))

temp = np.copy(binary)

while True:
    # Erode the image
    eroded = cv2.erode(temp, kernel)
    # Open the eroded image (erosion followed by dilation)
    opened = cv2.dilate(eroded, kernel)
    # Subtract opened from original temp to get skeleton part
    temp_diff = cv2.subtract(temp, opened)
    # Add to skeleton image
    skeleton = cv2.bitwise_or(skeleton, temp_diff)
    # Update temp
    temp = np.copy(eroded)

    # Stop if image is fully eroded
    if cv2.countNonZero(temp) == 0:
        break

# Show and save result
cv2.imshow("Binary Image", binary)
cv2.imshow("Skeleton", skeleton)
cv2.imwrite("images/skeleton_output.jpg", skeleton)
cv2.waitKey(0)
cv2.destroyAllWindows()
