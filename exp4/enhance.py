import cv2

# Read the color image
img = cv2.imread(r'D:\Academic\Fourth year Second semester\4206\Code\exp4\rgb.jpg')
#img = cv2.imread(r'D:\Academic\Fourth year Second semester\4206\Code\exp4\gfg.png')  # IGNORE

if img is None:
    print("Image not found.")
    exit()

# Check if grayscale
if len(img.shape) == 2:
    # Grayscale enhancement
    enhanced = cv2.equalizeHist(img)

else:
    # Convert to LAB color space
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

    # Split channels
    l, a, b = cv2.split(lab)

    # Equalize the L channel
    l_eq = cv2.equalizeHist(l)

    # Merge the enhanced L with original a and b
    lab_eq = cv2.merge([l_eq, a, b])

    # Convert back to BGR
    enhanced = cv2.cvtColor(lab_eq, cv2.COLOR_LAB2BGR)

# Save and show
cv2.imwrite('images/enhanced_color.jpg', enhanced)
cv2.imshow("Original", img)
cv2.imshow("Enhanced", enhanced)
cv2.waitKey(0)
cv2.destroyAllWindows()
