import cv2
import numpy as np

gray = cv2.imread(r'D:\Academic\Fourth year Second semester\4206\Code\exp6\gfg.png', cv2.IMREAD_GRAYSCALE)

# Apply histogram equalization
enhanced = cv2.equalizeHist(gray)

cv2.imshow("Grayscale Original", gray)
cv2.imshow("Grayscale Enhanced", enhanced)
cv2.waitKey(0)
cv2.destroyAllWindows()
