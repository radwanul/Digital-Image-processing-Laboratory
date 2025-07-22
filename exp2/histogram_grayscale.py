import cv2
import matplotlib.pyplot as plt

# Load grayscale image
img = cv2.imread(r'D:\Academic\Fourth year Second semester\4206\Code\exp2\1713256915670.jpg', cv2.IMREAD_GRAYSCALE)

if img is None:
    print("❌ Image not found.")
    exit()

# Calculate histogram
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# Plot
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")
plt.plot(hist, color='black')
plt.xlim([0, 256])
plt.grid(True)
plt.show()
