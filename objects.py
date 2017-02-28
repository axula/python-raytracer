from Coord import Coord
from Ray import Ray
import math

class Object:
    def __init__(self, color, shape):
        self.color = color
        self.shape = shape

    def pointcolor(self, ambient_coefficient, diffuse_coefficient, shade):
        # returns the color for when the object is in shadow
        mod = ambient_coefficient + diffuse_coefficient * shade
        point_color = ( int(self.color[0] * mod), \
                        int(self.color[1] * mod), \
                        int(self.color[2] * mod) )
        return point_color

class Sphere:
    # def __init__(self, center, radius):
        # Object.__init__(self, color, "sphere")
    def __init__(self, center, radius, color):
        self.center = center
        self.radius = radius
        self.color = color

    def pointcolor(self, ambient_coefficient, diffuse_coefficient, shade):
        # returns the color for when the object is in shadow
        mod = ambient_coefficient + diffuse_coefficient * shade
        point_color = ( int(self.color[0] * mod), \
            int(self.color[1] * mod), \
            int(self.color[2] * mod) )
        return point_color

    def normal(self, point):
        # returns the normal for a point on the sphere
        return Ray(point1=self.center, point2=point)

    def ray_intersect(self, ray):
        # vector between vector origin and sphere center
        L = Coord(ray.origin.x - self.center.x,
                  ray.origin.y - self.center.y,
                  ray.origin.z - self.center.z)
        b = 2.0 * ray.unitvector.x * (L.x) + 2.0 * ray.unitvector.y * (L.y) + \
            2.0 * ray.unitvector.z * (L.z)
        c = self.center.x**2 + self.center.y**2 + self.center.z**2 + \
            ray.origin.x**2 + ray.origin.y**2 + ray.origin.z**2 + \
            -2.0 * (self.center.x * ray.origin.x + self.center.y * ray.origin.y + \
                  self.center.z * ray.origin.z) - self.radius**2
        d = b**2 - 4*c
        # If the discriminate is negative, there is no intersection
        if d < 0:
            return 0.0
        else:
            t0 = (-b - math.sqrt(d)) / 2.0
            if t0 >= 0.0:
                return t0
            t1 = (-b + math.sqrt(d)) / 2.0
            if t1 >= 0:
                return t1
            return 0.0

    def __str__(self):
        return "Sphere at %s, with radius %f" % (self.center, self.radius)

class Cylinder(Object):
    def __init__(self, center, height, radius):
        Object.__init__(self, color, "cylinder")
        self.center = center
        self.radius = float(radius)
        self.height = float(height)

    def ray_intersect(self, ray):
        pass

class Plane(Object):
    def __init__(self, points):
        Object.__init__(self, color, "plane")
        self.points = points
