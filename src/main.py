from task_12_2 import Circle
from task_12_2 import Point
from task_12_2 import Square
from task_12_2 import Triangle


circle1 = Circle(2.5)
triangle = Triangle(Point(2, 3), Point(4, 5), Point(2, 5))
square = Square(Point(1, 1), Point(4, 4))
figures = [circle1, triangle, square]

for i in figures:
    print(f'Периметр  равен:{i.perimetr()}')
    print(f'Площадь  равна: {i.square()}')
