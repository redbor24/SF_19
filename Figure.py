import math


class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_area(self):
        return self.length * self.width


class Square(Rectangle):
    def __init__(self, width):
        self.width = width

    def get_area(self):
        return self.width ** 2


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return round(2 * math.pi * self.radius ** 2, 4)