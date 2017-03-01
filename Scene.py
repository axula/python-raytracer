from Coord import Coord

class Scene:
    def __init__(self, width, height):
        # Components in scene
        self.camera = Coord(0, 0, 0)
        self.light = Coord(0, 0, 0)
        # self.lights = []
        self.objects = []

        # Frame Settings
        self.height = height
        self.width = width
        self.depth = 6
        self.unit = 0.005
        self.pixels = []

        # Miscellaneous Settings
        self.ambient_coefficient = 0.2
        self.shadow_bias = 1e-4
        self.blank_color = (0, 0, 0)

    def diffuse_coefficient(self):
        return 1 - self.ambient_coefficient
