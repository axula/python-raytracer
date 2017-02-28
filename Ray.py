from Coord import Coord
import math

class Ray:
    def __init__(self, point1, point2):
        self.origin = point1
        self.unitvector = self.calculate_unitvector(point1, point2)

    def intersect_point(self, dist):
        x = self.unitvector.x * dist + self.origin.x
        y = self.unitvector.y * dist + self.origin.y
        z = self.unitvector.z * dist + self.origin.z
        return Coord( x, y, z )

    # Caculates the unit vector given two points
    def calculate_unitvector(self, point1, point2):
        #first finds the directional vector
        d = Coord(point2.x - point1.x, point2.y - point1.y, point2.z - point1.z)
        # Calculates magnitude based on vector
        m = math.sqrt(d.x**2 + d.y**2 + d.z**2)
        # Calculates the unit vector
        u = Coord( d.x/m, d.y/m, d.z/m )
        return u

    def __str__(self):
        return str(self.unitvector)
