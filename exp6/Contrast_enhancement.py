from PIL import Image
from PIL import ImageEnhance

# Opens the image file
image = Image.open(r'D:\Academic\Fourth year Second semester\4206\Basic-Image-Processing-Lab-Code\ImageEnhancement\gfg.png')

# shows image in image viewer
image.show()


# Enhance Contrast
curr_con = ImageEnhance.Contrast(image)
#new_con = 0.3
new_con = 8.3

# Contrast enhanced by a factor of 0.3
img_contrasted = curr_con.enhance(new_con)

# shows updated image in image viewer
img_contrasted.show()
