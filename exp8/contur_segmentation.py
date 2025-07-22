import cv2

# Load image
img = cv2.imread(r'D:\Academic\Fourth year Second semester\4206\Code\exp8\itsohk.png')

if img is None:
    print("Image not found.")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply binary threshold
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Find contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours on the original image (in green)
img_with_contours = img.copy()
cv2.drawContours(img_with_contours, contours, -1, (0, 255, 0), 2)

# Show result
cv2.imshow("Original", img)
cv2.imshow("Contours", img_with_contours)
cv2.imwrite("images/contours_output.jpg", img_with_contours)
cv2.waitKey(0)
cv2.destroyAllWindows()
