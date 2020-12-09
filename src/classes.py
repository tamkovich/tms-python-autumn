"""Создать класс Point, описывающий точку(атрибуты: x, y). Создать класс
Figure. Создать три дочерних класса Circle(атрибуты: координаты
центра(тип Point), длина радиуса; методы: нахождение периметра и
площади окружности), Triangle(атрибуты: три точки, методы: нахождение
площади и периметра), Square(атрибуты: две точки, методы: нахождение
площади и периметра). При потребности создавать все необходимые
методы не описанные в задании. Создать список фигур и в цикле
подсчитать и вывести площади всех фигур на экран[my-oop-03]
Примечание: в рамках задание создать два файла: ​ classes.py ​ и m
​ ain.py ​ . В
первом будут описаны все классы, во втором классы будут
импортированы и использованы."""


class Point:
    """создаем класс Pet"""

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Figure:
    """создаем класс Figure"""


class Circle(Figure):
    """создаем класс Circle"""

    def __init__(self, center: Point, radius):
        self.center = center
        self.radius = radius

    def perimeter(self):
        """определение периметра"""
        return 2 * 3.14 * self.radius

    def square(self):
        """определение площади"""
        return 3.14 * self.radius ** 2


class Triangle(Figure):
    """создаем класс Triangle"""

    def __init__(self, a: Point, b: Point, c: Point):
        self.a = a
        self.b = b
        self.c = c
        self.line1 = ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5
        self.line2 = ((c.x - b.x) ** 2 + (c.y - b.y) ** 2) ** 0.5
        self.line3 = ((a.x - c.x) ** 2 + (a.y - c.y) ** 2) ** 0.5

    def perimeter(self):
        """определение периметра"""
        return self.line1 + self.line2 + self.line3

    def square(self):
        """определение площади"""
        p = 0.5 * (self.line1 + self.line2 + self.line3)
        s = (p * (p - self.line1) * (p - self.line2) * (p - self.line3)) ** 0.5
        return s


class Square:
    """создаем класс Square"""

    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b
        self.line1 = b.x - a.x
        self.line2 = b.y - a.y

    def square(self):
        """определение площади"""
        return self.line1 * self.line2

    def perimeter(self):
        """определение периметра"""
        return 2 * (self.line1 + self.line2)


