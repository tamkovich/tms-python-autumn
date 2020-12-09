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

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Figure:
    pass


class Circle(Figure):
    def __init__(self, radius, *args):
        self.central = args[0]
        self.radius = radius

    def perimeter(self):
        return 3.1415 *(self.radius * 2 )

    def square(self):
        return (self.radius ** 2) * 3.1415


class Triangle(Figure):
    def __init__(self, *args):
        self.point1 = args[0]
        self.point2 = args[1]
        self.point3 = args[2]
        self.side1 = (((self.point1.x - self.point2.x) ** 2 + (self.point1.y - self.point2.y) ** 2) ** (1/2))
        self.side2 = (((self.point2.x - self.point3.x) ** 2 + (self.point2.y - self.point3.y) ** 2) ** (1 / 2))
        self.side3 = (((self.point3.x - self.point1.x) ** 2 + (self.point3.y - self.point1.y) ** 2) ** (1 / 2))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def square(self):
        p = (self.side1 + self.side2 + self.side3) / 2
        return ( p * (p - self.side1) * (p - self.side2) * (p - self.side3) ** (1 / 2))


class Square(Figure):
    def __init__(self, *args):
        self.point1 = args[0]
        self.point2 = args[1]
        self.side1 = self.point1.x - self.point2.x
        self.side2 = self.point1.y - self.point2.y

    def perimeter(self):
        return (self.side1 + self.side2) * 2

    def square(self):
        return self.side1 * self.side2