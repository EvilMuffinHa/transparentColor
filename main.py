from PIL import Image
from numpy import array



p = input("What is the name of the image: ")
q = input("What is the name of the new image: ")
image = Image.open(p)
image = image.convert("RGBA")
red = int(input("Enter the red value: "))
rThreshold = int(input("Enter the red threshold: "))
green = int(input("Enter the green value: "))
gThreshold = int(input("Enter the green threshold: "))
blue = int(input("Enter the blue value: "))
bThreshold = int(input("Enter the blue threshold: "))
print("Replacing pixel")
newRed = int(input("Enter the new red value: "))
newGreen = int(input("Enter the new green value: "))
newBlue = int(input("Enter the new blue value: "))
newAlpha = int(input("Enter the new alpha value (0 or 1): "))
if newAlpha == 1:
    newAlpha = 255
img = array(image)
a, b, c = img.shape
for x in range(0, a):
    for y in range(0, b):
        pixels = img[x][y]
        if red - rThreshold < pixels[0] < red + rThreshold and \
                green - gThreshold < pixels[1] < green + gThreshold and \
                blue - bThreshold < pixels[2] < blue + bThreshold:
            newpixel = [newRed, newGreen, newBlue, newAlpha]
        else:
            newpixel = pixels
        img[x][y] = newpixel
replacedImage = Image.fromarray(img)
replacedImage.save(q)
