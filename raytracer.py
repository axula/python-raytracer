from PIL import Image
from Coord import Coord
from Ray import Ray
from objects import Sphere

def getpixel(ray, objects):
    # calculates the color of the current pixel based on interected objects
    intersect, dist = raytrace(ray, objects)
    if intersect:
        intersect_point = ray.intersect_point( dist )
        light_vector = Ray(point1=light, point2=intersect_point)
        normal_vector = intersect.normal(intersect_point)
        if inshadow(intersect_point, normal_vector, light_vector, objects):
            shade = 0.0
        else:
            shade = lambertshade(light_vector, normal_vector)
        point_color = intersect.pointcolor(ambient_coefficient, \
                        diffuse_coefficient, shade)
        return point_color # alter for shadow
    else:
        return (0, 0, 0)
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

def inshadow(intersect_point, normal, light_vector, objects):
    # given an object and light vector, checks whether or not the object is in shadow
    new_point = intersect_point.movepoint(normal, shadow_bias)
    master_dist = new_point.distance(light_vector.origin)
    for x in objects:
        dist = x.ray_intersect(light_vector)
        if dist !=0.0 and dist < master_dist:
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
light = Coord(-1.5, 1, 0)
ambient_coefficient = 0.2
diffuse_coefficient = 1.0 - ambient_coefficient
shadow_bias = 1e-4
objects = []
objects.append( Sphere( Coord(-0.5, 0, 10), 1, (255, 0, 0) ) )
objects.append( Sphere( Coord(0.5, 0, 16), 2, (0, 255, 0) ) )

# Set frame details
frame_width = 800 # in pixels
frame_height = 600 # in pixels
frame_depth = 6 # in units
frame_unit = 0.005

pixels = []
ypos = frame_height * frame_unit / 2.0

for y in range(frame_height):
    xpos = -frame_width * frame_unit / 2.0
    for x in range(frame_width):
        ray = Ray(point1=camera, point2=Coord(xpos, ypos, frame_depth))
        pixels.append( getpixel(ray, objects) )
        xpos += frame_unit
    ypos -= frame_unit

image = Image.new('RGB', (frame_width, frame_height))
image.putdata(pixels)
image.save('test.jpg')
