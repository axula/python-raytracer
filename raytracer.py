from PIL import Image
from Scene import Scene
from Coord import Coord
from Ray import Ray
from objects import Sphere, Plane

def createimage(scene):
    ypos = scene.height * scene.unit / 2.0
    for y in range(scene.height):
        xpos = -scene.width * scene.unit / 2.0
        for x in range(scene.width):
            ray = Ray(point1=scene.camera, point2=Coord(xpos, ypos, scene.depth))
            scene.pixels.append( getpixel(ray) )
            xpos += scene.unit
        ypos -= scene.unit

    image = Image.new('RGB', (scene.width, scene.height))
    image.putdata(scene.pixels)
    image.save('test.jpg')

def getpixel(ray):
    # calculates the color of the current pixel based on interected objects
    intersect, dist = raytrace(ray, scene.objects)
    if intersect:
        intersect_point = ray.intersect_point( dist )
        light_vector = Ray(point1=scene.light, point2=intersect_point)
        normal_vector = intersect.normal(intersect_point)
        if inshadow(intersect_point, normal_vector, light_vector, scene.objects):
            shade = 0.0
        else:
            shade = lambertshade(light_vector, normal_vector)
        point_color = intersect.pointcolor(scene.ambient_coefficient, \
                        scene.diffuse_coefficient(), shade)
        return point_color # alter for shadow
    else:
        return scene.blank_color
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
    new_point = intersect_point.movepoint(normal, scene.shadow_bias)
    master_dist = new_point.distance(light_vector.origin)
    for x in objects:
        dist = x.ray_intersect(light_vector)
        if dist !=0.0 and dist < master_dist:
            return True
    return False

def lambertshade(light_vector, normal_vector):
    shade = light_vector.scale(-1).dotproduct(normal_vector)
    if shade < 0:
        shade = 0.0
    return shade

scene = Scene(800, 600)
scene.light = Coord(-2, 6, 0)
scene.objects.append( Sphere( Coord(-0.5, 0.25, 10), 1, (255, 0, 0) ) )
scene.objects.append( Sphere( Coord(0.5, 0, 16), 2, (0, 255, 0) ) )
scene.objects.append( Plane( Coord(0, -2.0, 10), Coord(0, 1, 10), (0, 0, 255) ) )

createimage(scene)
