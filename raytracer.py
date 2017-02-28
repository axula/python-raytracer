from PIL import Image
from Coord import Coord
from Ray import Ray
from Sphere import Sphere

def getpixel(ray, objects):
    intersect, dist = raytrace(ray, objects)
    if intersect:
        intersect_point = ray.intersect_point( dist )
        print str(ray) + ", " + str(intersect_point)
        if inshadow(dist, intersect_point, light, objects):
            print "Shadow"
            pixels.append( intersect.shadow() ) # alter for shadow
        else:
            pixels.append( intersect.color )
    else:
        pixels.append( (0, 0, 0) )
    return

def raytrace(ray, objects):
    # given a ray, finds the object closest to the camera, if any
    last_intersect = None
    last_dist = None
    for x in objects:
        dist = x.ray_intersect(ray)
        # if the ray intersects and is closer
        if dist != 0 and \
            (last_intersect is None or dist < last_dist):
            last_intersect = x
            last_dist = dist
    return (last_intersect, last_dist)

def inshadow(intersect_dist, intersect_point, light, objects):
    # given an object and light, checks whether or not the object is in shadow
    ray = Ray(light, intersect_point) # vector between light and object
    for x in objects:
        dist = x.ray_intersect(ray)
        if dist !=0 and dist < intersect_dist:
            return True
    return False

camera = Coord(0, 0, 0)
light = Coord(-2, 0, 0)
objects = []
objects.append( Sphere( Coord(0, 0, 10), 1, (255, 0, 0) ) )
objects.append( Sphere( Coord(0.5, 0, 16), 2, (0, 255, 0) ) )

width = 200
height = 150

pixels = []
ypos = -height / 50 / 2.0

for y in range(height):
    xpos = -width / 50 / 2.0
    for x in range(width):
        ray = Ray(camera, Coord(xpos, ypos, 6))
        getpixel(ray, objects)
        xpos += 0.02
    ypos += 0.02

image = Image.new('RGB', (width, height))
image.putdata(pixels)
image.save('test.jpg')
