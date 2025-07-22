import cv2

# Load image
img = cv2.imread(r'D:\Academic\Fourth year Second semester\4206\Code\exp13\inp1.tif')

if img is None:
    print("Image not found.")
    exit()

# Apply average filter (5x5)
blurred = cv2.blur(img, (5, 5))

# Show and save
cv2.imshow("Original", img)
cv2.imshow("Average Blurred", blurred)
cv2.imwrite("images/average_blur_output.jpg", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
