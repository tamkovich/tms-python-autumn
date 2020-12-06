"""Создать класс Point, описывающий точку(атрибуты: x, y). Создать класс
Figure. Создать три дочерних класса Circle(атрибуты: координаты
центра(тип Point), длина радиуса; методы: нахождение периметра и
площади окружности), Triangle(атрибуты: три точки, методы: нахождение
площади и периметра), Square(атрибуты: две точки, методы: нахождение
площади и периметра). При потребности создавать все необходимые
методы не описанные в задании. Создать список фигур и в цикле
подсчитать и вывести площади всех фигур на экран[my-oop-03]"""

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Figure:
    def __init__(self, *args):
        self.args = args

class Circle(Figure):
    def __init__(self, x, y: Point, length_of_radius):
        self.x = x
        self.y = y
        self.length_of_radius = length_of_radius

    def calculate_area(self):
        return math.pi * self.length_of_radius ** 2

    def calculate_perimetr(self):
        return 2 * math.pi * self.length_of_radius



class Triangle(Figure):
    def __init__(self, A, B, C: Point):
        self.A = A
        self.B = B
        self.C = C
        self.first_side = ((self.B.x - self.A.x) ** 2 + (self.B.y - self.A.y) ** 2) ** 0.5
        self.second_side = ((self.B.x - self.C.x) ** 2 + (self.B.y - self.C.y) ** 2) ** 0.5
        self.third_side = ((self.C.x - self.A.x) ** 2 + (self.C.y - self.A.y) ** 2) ** 0.5

    def calculate_area(self) -> float:
        "Функция вычисляет площадь треугольника по формуле Герона"
        half_of_perimetr = (self.first_side + self.second_side + self.third_side) / 2
        return (half_of_perimetr * (half_of_perimetr - self.first_side) * (half_of_perimetr - self.second_side) * (half_of_perimetr - self.third_side)) ** 0.5

    def calculate_perimetr(self) -> float:
        "Функция вычисляет периметр треугольника"
        return self.first_side + self.second_side + self.third_side



class Square:
        def __init__(self, point_a, point_b: Point):
            self. point_a = point_a
            self.point_b = point_b

        def calculate_perimetr(self) -> float:
            "Функция вычисляет периметр квадрата"
            side = ((self.point_b.x - self.point_a.x) ** 2 + (self.point_b.y - self.point_a.y) ** 2) ** 0.5
            return side * 4

        def calculate_area(self) -> float:
            "Функция вычисляет площадь квадрата"
            side = ((self.point_b.x - self.point_a.x) ** 2 + (self.point_b.y - self.point_a.y) ** 2) ** 0.5
            return side ** 2
