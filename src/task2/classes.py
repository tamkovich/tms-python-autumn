import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Figure:
    pass


class Circle(Figure):
    def __init__(self, radius, *args):
        self.radius = radius
        self.center = args[0]

    def find_perimeter(self):
        return 2 * self.radius * math.pi

    def find_square(self):
        return math.pi * self.radius ** 2


class Triangle(Figure):
    def __init__(self, *args):
        point = args[0]
        point1 = args[1]
        point2 = args[2]
        self.first = (
            (point1.x - point.x) ** 2 + (point1.y - point.y) ** 2
        ) ** (1 / 2)
        self.second = (
            (point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2
        ) ** (1 / 2)
        self.third = (
            (point2.x - point.x) ** 2 + (point2.y - point.y) ** 2
        ) ** (1 / 2)

    def find_square(self):
        p = (self.first + self.second + self.third) / 2
        return (
            p * (p - self.first) * (p - self.second) * (p - self.third)
        ) ** (1 / 2)

    def find_perimeter(self):
        return self.first + self.second + self.third


class Square(Figure):
    def __init__(self, *args):
        point1 = args[0]
        point2 = args[1]
        self.first = math.fabs(point2.x - point1.x)
        self.second = math.fabs(point2.y - point1.y)

    def find_square(self):
        return self.first * self.second

    def find_perimeter(self):
        return 2 * (self.first + self.second)
