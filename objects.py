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

    def dotproduct(self, a, b):
        return (a.unitvector.x * b.unitvector.x) + \
               (a.unitvector.y * b.unitvector.y) + \
               (a.unitvector.z * b.unitvector.z)

class Sphere(Object):
    def __init__(self, center, radius, color):
        Object.__init__(self, color, "sphere")
        self.center = center
        self.radius = radius

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
    def __init__(self, center, height, radius, color):
        Object.__init__(self, color, "cylinder")
        self.center = center # base of cylinder, in the center of the "cap"
        self.radius = radius
        self.height = height # extends in the normal direction from the center

    def ray_intersect(self, ray):
        pass

class Plane(Object):
    def __init__(self, point1, point2, color):
        Object.__init__(self, color, "plane")
        self.point = point1
        self.normal_vector = Ray(point1=point1, point2=point2)

    def normal(self, point):
        return self.normal_vector

    def ray_intersect(self, ray):
        denom = self.normal_vector.dotproduct(ray)
        if denom !=0:
            t = ( ray.origin.directionvector(self.point) ).\
                    dotproduct( self.normal_vector ) / denom
            if t >= 0:
                return t
        return 0.0
