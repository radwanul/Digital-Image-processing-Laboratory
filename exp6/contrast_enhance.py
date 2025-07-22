import cv2
import numpy as np

# Load image
img = cv2.imread(r'D:\Academic\Fourth year Second semester\4206\Code\exp6\gfg.png')  # use your file name

if img is None:
    print("Image not found.")
    exit()

# Set contrast value
alpha = 1.5  # Try values from 1.0 to 3.0

# Apply contrast scaling
# Convert to float for precision, then clip and convert back
enhanced = np.clip(alpha * img, 0, 255).astype(np.uint8)

# Show and save
cv2.imshow("Original", img)
cv2.imshow("Contrast Enhanced", enhanced)
cv2.imwrite("images/contrast_enhanced.jpg", enhanced)
cv2.waitKey(0)
cv2.destroyAllWindows()
