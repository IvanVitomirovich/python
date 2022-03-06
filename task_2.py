class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def road_weight(self, s_grav, thickness):
        return self._length * self._width * s_grav * thickness / 1000


r = Road(5000, 20)
print(r.road_weight(25, 5))
