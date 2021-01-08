from classes import Circle
from classes import Point
from classes import Square
from classes import Triangle


circle1 = Circle(Point(2, 3), 24)
triangle1 = Triangle(Point(1, 19), Point(8, 16), Point(6, 8))
sqr1 = Square(Point(2, 3), Point(15, 20))

figures = [circle1, triangle1, sqr1]

for i in figures:
    print(f"Периметр  равен:{i.perimeter()}")
    print(f"Площадь  равна: {i.square()}")
