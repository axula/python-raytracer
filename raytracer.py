from PIL import Image
from Coord import Coord
from Ray import Ray
from Sphere import Sphere

camera = Coord(0, 0, 0)
sphere = Sphere( Coord(0, 0, 10), 0.5 )

width = 200
height = 150

pixels = []
ypos = -height / 50 / 2.0

for y in range(height):
    xpos = -width / 50 / 2.0
    for x in range(width):
        ray = Ray(camera, Coord(xpos, ypos, 6))
        if sphere.does_ray_intersect(ray):
            pixels.append( (255, 255, 255) )
        else:
            pixels.append( (0, 0, 0) )
        xpos += 0.02
    ypos += 0.02

image = Image.new('RGB', (width, height))
image.putdata(pixels)
image.save('test.jpg')
