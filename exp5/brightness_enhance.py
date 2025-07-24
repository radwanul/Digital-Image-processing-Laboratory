from PIL import Image
from PIL import ImageEnhance

# Opens the image file
image = Image.open(r'D:\Academic\Fourth year Second semester\4206\Basic-Image-Processing-Lab-Code\ImageEnhancement\gfg.png')

# shows image in image viewer
image.show()


# Enhance Brightness
curr_bri = ImageEnhance.Brightness(image)
new_bri = 2.5

# Brightness enhanced by a factor of 2.5
img_brightened = curr_bri.enhance(new_bri)

# shows updated image in image viewer
img_brightened.show()
