import math

class Coord:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def movepoint(self, vector, dist):
        x = vector.unitvector.x * dist + self.x
        y = vector.unitvector.y * dist + self.y
        z = vector.unitvector.z * dist + self.z
        return Coord( x, y, z )

    def directionvector(self, point2):
        return Coord(point2.x - self.x, point2.y - self.y, point2.z - self.z)

    def dotproduct(self, b):
        return (self.x * b.x) + \
               (self.y * b.y) + \
               (self.z * b.z)

    def distance(self, point):
        d = Coord(self.x - point.x, self.y - point.y, self.z - point.z)
        return math.sqrt(d.x**2 + d.y**2 + d.z**2)

    def __str__(self):
        return "(%f, %f, %f)" % (self.x, self.y, self.z)
