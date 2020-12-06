"""Создать класс Point, описывающий точку(атрибуты: x, y). Создать класс
Figure. Создать три дочерних класса Circle(атрибуты: координаты
центра(тип Point), длина радиуса; методы: нахождение периметра и
площади окружности), Triangle(атрибуты: три точки, методы: нахождение
площади и периметра), Square(атрибуты: две точки, методы: нахождение
площади и периметра). При потребности создавать все необходимые
методы не описанные в задании. Создать список фигур и в цикле
подсчитать и вывести площади всех фигур на экран[my-oop-03]
Примечание: в рамках задание создать два файла: classes.py и main.py. В
первом будут описаны все классы, во втором классы будут
импортированы и использованы."""


from classes import Circle
from classes import Triangle
from classes import Point
from classes import Square

circle1 = Circle(3, Point(1, 2))
print(circle1.perim())
print(circle1.square())

triangle1 = Triangle(Point(1, 1), Point(3, 4), Point(2, 2))
print(triangle1.perim())
print(triangle1.square())

square1 = Square(Point(1, 1), Point(3, 4))
print(square1.perim())
print(square1.square())
