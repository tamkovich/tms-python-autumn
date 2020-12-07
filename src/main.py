from classes import Point
from classes import triangle
from classes import Circle
from classes import Square

krug = Circle(3, Point(1, 2))
print(krug.perimetr())
print(krug.square())

tre = triangle(Point(1, 1), Point(3, 4), Point(2, 2))
print(tre.perimetr())
print(tre.square())

quadratic = Square(Point(1, 1), Point(3, 4))
print(quadratic.perimetr())
print(quadratic.square())
