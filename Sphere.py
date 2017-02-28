from Coord import Coord
from Ray import Ray
import math

class Sphere:
    def __init__(self, coord, r, color):
        self.pos = coord
        self.radius = r
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
        return Ray(point1=self.pos, point2=point)

    def ray_intersect(self, ray):
        # vector between vector origin and sphere pos
        L = Coord(ray.origin.x - self.pos.x,
                  ray.origin.y - self.pos.y,
                  ray.origin.z - self.pos.z)
        b = 2.0 * ray.unitvector.x * (L.x) + 2.0 * ray.unitvector.y * (L.y) + \
            2.0 * ray.unitvector.z * (L.z)
        c = self.pos.x**2 + self.pos.y**2 + self.pos.z**2 + \
            ray.origin.x**2 + ray.origin.y**2 + ray.origin.z**2 + \
            -2.0 * (self.pos.x * ray.origin.x + self.pos.y * ray.origin.y + \
                  self.pos.z * ray.origin.z) - self.radius**2
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
        return "Sphere at %s, with radius %f" % (self.pos, self.radius)
