from PIL import Image
from Sphere import Sphere

width = 800
height = 600

old = Image.open('test.jpg')
old_pixels = list(old.getdata())
print old_pixels[0]

pixels = []
for x in range(width):
    for y in range(height):
        pixels.append( (255, 255, 255) )

image = Image.new('RGB', (width, height))
image.putdata(pixels)
image.save('test.jpg')
