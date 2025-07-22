import cv2
import numpy as np

# Load the image
img = cv2.imread(r'D:\Academic\Fourth year Second semester\4206\Code\exp9\itsohk.png')

if img is None:
    print("Image not found.")
    exit()

# Reshape image to a 2D array of pixels (each with 3 values: R,G,B)
Z = img.reshape((-1, 3))
Z = np.float32(Z)  # convert to float32

# Define criteria (type, max_iter, epsilon)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

K = 4  # Number of clusters
_, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Convert centers to 8-bit (0-255), and replace each pixel with its center color
center = np.uint8(center)
segmented = center[label.flatten()]
segmented_img = segmented.reshape((img.shape))

# Show result
cv2.imshow('Original', img)
cv2.imshow('Segmented (K-Means)', segmented_img)
cv2.imwrite('images/kmeans_output.jpg', segmented_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
