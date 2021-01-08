'''Создать класс Point, описывающий точку(атрибуты: x, y). Создать класс
Figure. Создать три дочерних класса Circle(атрибуты: координаты
центра(тип Point), длина радиуса; методы: нахождение периметра и
площади окружности), Triangle(атрибуты: три точки, методы: нахождение
площади и периметра), Square(атрибуты: две точки, методы: нахождение
площади и периметра). При потребности создавать все необходимые
методы не описанные в задании. Создать список фигур и в цикле
подсчитать и вывести площади всех фигур на экран'''

from math import fabs


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Figure:
    pass


class Circle(Point):
    def __init__(self, r: float):
        self.r = r

    def perimetr(self):
        return self.r * 2 * 3.1415

    def square(self):
        return 3.1415 * self.r ** 2


class Triangle:
    def __init__(self, point_a: 'Point', point_b: 'Point', point_c: 'Point'):
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c
        self.len_line1 = (
            (point_a.x - point_b.x) ** 2 + (point_a.y - point_b.y) ** 2
        ) ** 1 / 2
        self.len_line2 = (
            (point_c.x - point_b.x) ** 2 + (point_c.y - point_b.y) ** 2
        ) ** 1 / 2
        self.len_line3 = (
            (point_a.x - point_c.x) ** 2 + (point_a.y - point_c.y) ** 2
        ) ** 1 / 2

    def perimetr(self):
        return self.len_line1 + self.len_line2 + self.len_line3

    def square(self):
        return (fabs(
            (self.point_a.x - self.point_b.x
             ) * (self.point_c.y - self.point_b.y
                  ) - (self.point_c.x - self.point_b.x
                       ) * (self.point_a.y - self.point_b.y))) / 2


class Square:
    def __init__(self, point_a: 'Point', point_b: 'Point'):
        self.point_a = point_a
        self.point_b = point_b
        self.diag = (
            (point_b.x - point_a.x) ** 2 + (point_b.y - point_a.y) ** 2
        ) ** 1 / 2

    def square(self):
        return (self.diag ** 2) / 2

    def perimetr(self):
        return 2 * (2 * self.diag) ** 1 / 2
