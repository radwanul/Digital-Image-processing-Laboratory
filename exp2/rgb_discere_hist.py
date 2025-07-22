import cv2
import matplotlib.pyplot as plt

# Load image in color
#img = cv2.imread(r'D:\Academic\Fourth year Second semester\4206\Code\exp2\1713256915670.jpg')
img = cv2.imread(r'D:\Academic\Fourth year Second semester\4206\Code\exp2\hist2.tif')

# Split channels
b, g, r = cv2.split(img)

# Plot histogram for each channel using plt.hist()
plt.figure(figsize=(10,5))
plt.title("RGB Histogram (Discrete)")
plt.xlabel("Pixel Intensity")
plt.ylabel("Pixel Count")

plt.hist(r.ravel(), 256, [0, 256], color='red', alpha=0.5, label='Red')
plt.hist(g.ravel(), 256, [0, 256], color='green', alpha=0.5, label='Green')
plt.hist(b.ravel(), 256, [0, 256], color='blue', alpha=0.5, label='Blue')

plt.legend()
plt.grid(True)
plt.show()
