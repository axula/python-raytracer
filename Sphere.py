from Coord import Coord
from Ray import Ray
import math

class Sphere:
    def __init__(self, coord, r):
        self.pos = coord
        self.radius = r

    def does_ray_intersect(self, ray):
        # vector between camera and sphere pos
        L = Coord(ray.origin.x-self.pos.x, 
                  ray.origin.y-self.pos.y, 
                  ray.origin.z-self.pos.z)
        b = 2.0 * ray.unitvector.x * (L.x) + 2.0 * ray.unitvector.y * (L.y) + \
            2.0 * ray.unitvector.z * (L.z)
        c = self.pos.x**2 + self.pos.y**2 + self.pos.z**2 + \
            ray.origin.x**2 + ray.origin.y**2 + ray.origin.z**2 + \
            -2.0 * (self.pos.x * ray.origin.x + self.pos.y * ray.origin.y + \
                  self.pos.z * ray.origin.z) - self.radius**2
        d = b**2 - 4*c
        # If the discriminate is negative, there is no intersection
        if d < 0:
            return False
        else:
            return True
        '''
        t0 = (-b - math.sqrt(d)) / 2
        t1 = (-b + math.sqrt(d)) / 2
        '''
