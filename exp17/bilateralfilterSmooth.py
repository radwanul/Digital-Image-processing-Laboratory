import cv2

# Load image
img = cv2.imread(r'D:\Academic\Fourth year Second semester\4206\Code\exp17\inp3.tif')

if img is None:
    print("Image not found.")
    exit()

# Apply bilateral filter
filtered = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)

# Show and save result
cv2.imshow("Original", img)
cv2.imshow("Bilateral Filtered", filtered)
cv2.imwrite("images/bilateral_filtered.jpg", filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()
