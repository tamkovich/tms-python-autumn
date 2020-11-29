# Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость(по
# умолчанию 0). Методы: увеличить скорости(скорость + 5), уменьшение
# скорости(скорость - 5), стоп(сброс скорости на 0), отображение скорости,
# разворот(изменение знака скорости). Все атрибуты приватные.

class Car:
    def __init__(self, tupe, model, year, speed=0):
        self.__tupe = tupe
        self.__model = model
        self.__year = year
        self.__speed = speed

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        self.__speed = speed

    def up_speed(self):
        self.__speed += 5

    def low_speed(self):
        self.__speed -= 5

    def stop_speed(self):
        self.__speed = 0

    def rev_speed(self):
        self.__speed *= -1


car = Car('bmw', 'x5', '2020')
print(car.get_speed())
car.up_speed()
print(car.get_speed())
car.up_speed()
print(car.get_speed())
car.low_speed()
print(car.get_speed())
car.rev_speed()
print(car.get_speed())
car.stop_speed()
print(car.get_speed())
