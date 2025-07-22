import cv2
import matplotlib.pyplot as plt

# Load color image
img = cv2.imread(r'D:\Academic\Fourth year Second semester\4206\Code\exp2\1713256915670.jpg')

if img is None:
    print("Image not found.")
    exit()

# Plot histogram for each color channel
colors = ('b', 'g', 'r')
plt.figure()
plt.title("RGB Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")

for i, col in enumerate(colors):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.grid(True)
plt.show()
