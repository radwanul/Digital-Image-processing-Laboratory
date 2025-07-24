from PIL import Image
from PIL import ImageEnhance

# Opens the image file
image = Image.open(r'D:\Academic\Fourth year Second semester\4206\Basic-Image-Processing-Lab-Code\ImageEnhancement\gfg.png')

# shows image in image viewer
image.show()


# Enhance Color Level
curr_col = ImageEnhance.Color(image)
new_col = 6

# Color level enhanced by a factor of 2.5
img_colored = curr_col.enhance(new_col)

# shows updated image in image viewer
img_colored.show()
