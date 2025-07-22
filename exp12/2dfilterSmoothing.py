import cv2
import numpy as np

# Load image
img = cv2.imread(r'D:\Academic\Fourth year Second semester\4206\Code\exp12\inp3.tif')

if img is None:
    print("Image not found.")
    exit()

# Define a 3x3 averaging kernel (everything gets equal weight)
kernel = np.ones((3, 3), np.float32) / 9

# Apply 2D convolution
smoothed = cv2.filter2D(img, -1, kernel)

# Show and save
cv2.imshow("Original", img)
cv2.imshow("Smoothed with 2D Filter", smoothed)
cv2.imwrite("images/smooth_2d_output.jpg", smoothed)
cv2.waitKey(0)
cv2.destroyAllWindows()
