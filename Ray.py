from Coord import Coord
import math

class Ray:
    def __init__(self, *args, **kwargs):
        if 'point1' in kwargs:
            self.origin = kwargs['point1']
            self.unitvector = self.calculate_unitvector(self.origin, kwargs['point2'])
        elif 'origin' in kwargs:
            self.origin = kwargs['origin']
            self.unitvector = kwargs['vector']
        self.x = self.unitvector.x
        self.y = self.unitvector.y
        self.z = self.unitvector.z

    def scale(self, num):
        x = self.x * num
        y = self.y * num
        z = self.z * num
        return Ray( origin=self.origin, vector=Coord(x, y, z) )

    def dotproduct(self, b):
        return (self.x * b.x) + \
               (self.y * b.y) + \
               (self.z * b.z)

    def intersect_point(self, dist):
        x = self.unitvector.x * dist + self.origin.x
        y = self.unitvector.y * dist + self.origin.y
        z = self.unitvector.z * dist + self.origin.z
        return Coord( x, y, z )

    # Caculates the unit vector given two points
    def calculate_unitvector(self, point1, point2):
        #first finds the directional vector
        d = point1.directionvector(point2)
        # Calculates magnitude based on vector
        m = math.sqrt(d.x**2 + d.y**2 + d.z**2)
        # Calculates the unit vector
        u = Coord( d.x/m, d.y/m, d.z/m )
        return u

    def __str__(self):
        return str(self.unitvector)
