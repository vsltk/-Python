class Road:
    def __init__(self, length, width):
        self._lenght = length
        self._width = width

    def creating_a_road(self, weight = 25, thickness = 5):
        return f"{(self._lenght * self._width * weight * thickness) / 1000} тонн."

r = Road(5000, 20)
print(r.creating_a_road())