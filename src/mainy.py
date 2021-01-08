from classes import Circle
from classes import Point
from classes import Square
from classes import Triangle


circle1 = Circle(Point(2, 6), 14)
triangle1 = Triangle(Point(4, 10), Point(10, 18), Point(16, 12))
sqr1 = Square(Point(1, 1), Point(4, 4))
figures = [circle1, triangle1, sqr1]

print(f"Периметр круга равен {circle1.perimeter()}")
print(f"Площадь круга равна {circle1.square()}")
print(f"Периметр треугольника равен {triangle1.perimeter()}")
print(f"Площадь треугольника равна {triangle1.square()}")
print(f"Периметр квадрата равен {sqr1.perimeter()}")
print(f"Площадь квадрата равна {sqr1.square()}")
