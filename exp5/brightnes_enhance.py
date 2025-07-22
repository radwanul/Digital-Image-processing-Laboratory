import cv2
import numpy as np

# Load image
img = cv2.imread(r'D:\Academic\Fourth year Second semester\4206\Code\exp5\rgb.jpg')

if img is None:
    print("Image not found.")
    exit()

# Convert to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Split channels
h, s, v = cv2.split(hsv)

# Increase brightness by adding a value (but clip to 255)
value = 10
v = np.clip(v + value, 0, 255).astype(np.uint8)

# Merge and convert back
hsv_enhanced = cv2.merge((h, s, v))
bright_img = cv2.cvtColor(hsv_enhanced, cv2.COLOR_HSV2BGR)

# Show and save
cv2.imshow("Original", img)
cv2.imshow("Brightness Enhanced", bright_img)
cv2.imwrite("images/brightened_image.jpg", bright_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
