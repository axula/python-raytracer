from Coord import Coord
from Ray import Ray
import math

class Sphere:
    def __init__(self, coord, r, color):
        self.pos = coord
        self.radius = r
        self.color = color

    def ray_intersect(self, ray):
        # vector between camera and sphere pos
        L = Coord(self.pos.x - ray.origin.x, 
                  self.pos.y - ray.origin.y, 
                  self.pos.z - ray.origin.z)
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
