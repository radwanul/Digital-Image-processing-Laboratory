import cv2

# Load image
img = cv2.imread(r'D:\Academic\Fourth year Second semester\4206\Code\exp15\inp3.tif')

if img is None:
    print("Image not found.")
    exit()

# Apply median filter
median = cv2.medianBlur(img, 5)  # kernel size must be odd and > 1

# Show and save
cv2.imshow("Original", img)
cv2.imshow("Median Blurred", median)
cv2.imwrite("images/median_blur_output.jpg", median)
cv2.waitKey(0)
cv2.destroyAllWindows()
