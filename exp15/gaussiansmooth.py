import cv2

# Load the image
img = cv2.imread(r'D:\Academic\Fourth year Second semester\4206\Code\exp14\inp1.tif')

if img is None:
    print("Image not found.")
    exit()

# Apply Gaussian Blur
gaussian = cv2.GaussianBlur(img, (5, 5), 0)  # (kernel size, sigma)

# Show and save
cv2.imshow("Original", img)
cv2.imshow("Gaussian Blurred", gaussian)
cv2.imwrite("images/gaussian_blur_output.jpg", gaussian)
cv2.waitKey(0)
cv2.destroyAllWindows()
