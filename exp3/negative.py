import cv2

# Read image (color or grayscale)
image = cv2.imread(r'D:\Academic\Fourth year Second semester\4206\Code\exp3\rgb.jpg')

# Just subtract from 255
negative = 255 - image

# Show both
cv2.imshow('Original', image)
cv2.imshow('Negative', negative)
cv2.waitKey(0)
cv2.destroyAllWindows()
