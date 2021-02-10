import math

class GeomFigure:
    def get_area(self):
        return "<abstract method>"

    def __str__(self):
        return f"{self.__class__.__name__} ()"


class Rectangle(GeomFigure):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_area(self):
        return self.length * self.width

    def __str__(self):
        return f"{self.__class__.__name__} ({self.width}, {self.length})"


class Square(GeomFigure):
    def __init__(self, width):
        self.width = width

    def get_area(self):
        return self.width ** 2

    def __str__(self):
        return f"{self.__class__.__name__} ({self.width})"


class Circle(GeomFigure):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return round(2 * math.pi * self.radius ** 2, 4)

    def __str__(self):
        return f"{self.__class__.__name__} ({self.radius})"

