#image processing
from PIL import Image  

import glob

#identify, return and print pathnames ending wuth .png
print(glob.glob("*.png"))

#iterates through image files in current working directory
for file in glob.glob("*.png"):
#open image file
    im = Image.open(file)
