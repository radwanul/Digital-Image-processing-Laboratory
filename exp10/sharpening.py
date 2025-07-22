import cv2
import numpy as np

# Load image (color or grayscale)
img = cv2.imread(r'D:\Academic\Fourth year Second semester\4206\Code\exp10\inp1.jpg')  # replace with your image

if img is None:
    print("❌ Image not found.")
    exit()

# Define sharpening kernel
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])

# Apply filter
sharpened = cv2.filter2D(img, -105, kernel)

# Show and save
cv2.imshow("Original", img)
cv2.imshow("Sharpened", sharpened)
cv2.imwrite("D:\Academic\Fourth year Second semester\4206\Code\exp10/sharpened_output.jpg", sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
