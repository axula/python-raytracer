from PIL import Image
from Coord import Coord
from Ray import Ray
from Sphere import Sphere

def raytrace(ray, objects):
    last_intersect = None
    last_dist = None
    for x in objects:
        dist = x.ray_intersect(ray)
        # if the ray intersects and is closer
        if dist != 0 and \
            (last_intersect is None or dist < last_dist):
            last_intersect = x
            last_dist = dist
    if last_intersect:
        pixels.append( last_intersect.color )
    else:
        pixels.append( (0, 0, 0) )
    return

camera = Coord(0, 0, 0)
objects = []
objects.append( Sphere( Coord(0, 0, 10), 0.5, (255, 0, 0) ) )
objects.append( Sphere( Coord(0.5, 0, 16), 1, (0, 255, 0) ) )

width = 200
height = 150

pixels = []
ypos = -height / 50 / 2.0

for y in range(height):
    xpos = -width / 50 / 2.0
    for x in range(width):
        ray = Ray(camera, Coord(xpos, ypos, 6))
        raytrace(ray, objects)
        xpos += 0.02
    ypos += 0.02

image = Image.new('RGB', (width, height))
image.putdata(pixels)
image.save('test.jpg')
