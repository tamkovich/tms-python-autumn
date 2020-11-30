"""Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость(по
умолчанию 0). Методы: увеличить скорости(скорость + 5), уменьшение
скорости(скорость - 5), стоп(сброс скорости на 0), отображение скорости,
разворот(изменение знака скорости). Все атрибуты приватные."""


class Car:
    def __init__(self, mark, model, year, speed=0):
        self.__mark = mark
        self.__model = model
        self.__year = year
        self.__speed = speed

    def speed(self):
        print(self.__speed)

    def razvorot(self):
        self.__speed = - self.__speed

    def incr_speed(self):
        if self.__speed >= 0:
            self.__speed += 5
        else:
            self.__speed += - 5

    def decr_speed(self, speed):
        if self.__speed >= 0:
            self.__speed = speed - 5
        else:
            self.__speed = speed + 5

    def breaking(self):
        self.__speed = 0


car1 = Car("BMW", "5", "2018")
car1.speed()
car1.incr_speed()
car1.speed()
car1.incr_speed()
car1.speed()
car1.razvorot()
car1.speed()
car1.incr_speed()
car1.speed()
car1.breaking()
car1.speed()
