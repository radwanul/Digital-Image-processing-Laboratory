import cv2

# Load grayscale image
img = cv2.imread(r'D:\Academic\Fourth year Second semester\4206\Code\exp7\itsohk.png', cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Image not found.")
    exit()

# Apply thresholding
thresh_val = 127
_, thresholded = cv2.threshold(img, thresh_val, 255, cv2.THRESH_BINARY)

# Show and save
cv2.imshow("Original Grayscale", img)
cv2.imshow("Thresholded Image", thresholded)
cv2.imwrite("images/threshold_output.jpg", thresholded)
cv2.waitKey(0)
cv2.destroyAllWindows()



# _, otsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# cv2.imshow("Otsu Threshold", otsu)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
