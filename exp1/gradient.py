import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image in grayscale
img = cv2.imread(r'D:\Academic\Fourth year Second semester\4206\Code\exp1\lena.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Sobel operator in X and Y directions
grad_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
grad_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# Compute gradient magnitude
gradient = cv2.magnitude(grad_x, grad_y)

# Convert to 8-bit for display/saving
gradient = cv2.convertScaleAbs(gradient)

# Save and display
cv2.imwrite("images/gradient_output.jpg", gradient)

# Display using matplotlib
plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray'), plt.title('Original'), plt.axis('off')
plt.subplot(1, 3, 2), plt.imshow(grad_x, cmap='gray'), plt.title('Sobel X'), plt.axis('off')
plt.subplot(1, 3, 3), plt.imshow(gradient, cmap='gray'), plt.title('Gradient Magnitude'), plt.axis('off')
plt.tight_layout()
plt.show()
