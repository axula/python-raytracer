from PIL import Image
from Coord import Coord
from Ray import Ray
from Sphere import Sphere

def getpixel(ray, objects):
    intersect, dist = raytrace(ray, objects)
    if intersect:
        intersect_point = ray.intersect_point( dist )
        light_vector = Ray(point1=light, point2=intersect_point)
        normal_vector = intersect.normal(intersect_point)
        if inshadow(dist, intersect_point, light_vector, objects):
            shade = 0.0
        else:
            shade = lambertshade(light_vector, normal_vector)
        point_color = intersect.pointcolor(ambient_coefficient, \
            diffuse_coefficient, shade)
        pixels.append( point_color ) # alter for shadow
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

def inshadow(intersect_dist, intersect_point, ray, objects):
    # given an object and light vector, checks whether or not the object is in shadow
    for x in objects:
        dist = x.ray_intersect(ray)
        if dist !=0 and dist < intersect_dist:
            return True
    return False

def dotproduct(a, b):
    return (a.unitvector.x * b.unitvector.x) + \
           (a.unitvector.y * b.unitvector.y) + \
           (a.unitvector.z * b.unitvector.z)

def lambertshade(light_vector, normal_vector):
    shade = dotproduct(light_vector.scale(-1), normal_vector)
    if shade < 0:
        shade = 0.0
    return shade

camera = Coord(0, 0, 0)
light = Coord(-2, 0, 0)
ambient_coefficient = 0.2
diffuse_coefficient = 1.0 - ambient_coefficient
objects = []
objects.append( Sphere( Coord(0, 0, 10), 1, (255, 0, 0) ) )
objects.append( Sphere( Coord(0.5, 0, 16), 2, (0, 255, 0) ) )

width = 800
height = 600

pixels = []
ypos = height / 200 / 2.0

for y in range(height):
    xpos = -width / 200 / 2.0
    for x in range(width):
        ray = Ray(point1=camera, point2=Coord(xpos, ypos, 6))
        getpixel(ray, objects)
        xpos += 0.005
    ypos -= 0.005

image = Image.new('RGB', (width, height))
image.putdata(pixels)
image.save('test.jpg')
