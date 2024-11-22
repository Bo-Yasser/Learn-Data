# Image
# show()
# crop()
# rotate()
# convert()
# transpose()

# from PIL import Image


# myImage = Image.open(r"C:\Users\Smart Laptop\Downloads\ninja.jpg")


# myImage.show()


# myBox = (0, 0, 400, 400)

# myNewImage = myImage.crop(myBox)

# myNewImage.show()



# myConverted = myImage.convert("L")

# myConverted.show()




############################ pillow practice ############################ 

# 1


from PIL import Image

# open Image
file = Image.open(r"H:\Python\Photos\elzero-pillow.png")

# cut L letter
l_box = (400, 0, 800, 400)

l_cropped = file.crop(l_box)

# convert L
l_cropped_coverted = l_cropped.convert("L")

# show L
l_cropped_coverted.show()



# cut half 
half_box = (0, 400, 1200, 800)

half_cropped = file.crop(half_box)

# convert half
half_cropped_converted = half_cropped.convert("L")

# rotate half
half_cropped_converted_rotate = half_cropped_converted.rotate(180)   #or# half_cropped_converted.transpose(3)

# show half

half_cropped_converted_rotate.show()