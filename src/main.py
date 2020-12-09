# Создать класс Point, описывающий точку(атрибуты: x, y). Создать класс
# Figure. Создать три дочерних класса Circle(атрибуты: координаты
# центра(тип Point), длина радиуса; методы: нахождение периметра и
# площади окружности), Triangle(атрибуты: три точки, методы: нахождение
# площади и периметра), Square(атрибуты: две точки, методы: нахождение
# площади и периметра). При потребности создавать все необходимые
# методы не описанные в задании. Создать список фигур и в цикле
# подсчитать и вывести площади всех фигур на экран[my-oop-03]
# Примечание: в рамках задание создать два файла: classes.py  и main.py . В
# первом будут описаны все классы, во втором классы будут
# импортированы и использованы.


from classes import Circle
from classes import Triangle
from classes import Square
from classes import Point


circle1 = Circle(3, Point(2, 4))
print('Perimeter kruga: ',circle1.perimeter())
print('Ploshca kruga: ',circle1.square())

triangle1 = Triangle(Point(1,1), Point(2,2), Point(3,3))
print('Ploshca treugolnika: ',triangle1.square())
print('Perimeter treugolnika: ',triangle1.perimeter())

square1 = Square(Point(1,1), Point(5,6))
print('Ploshca kvadrata: ',square1.square())
print('Perimeter kvadrata: ',square1.perimeter())