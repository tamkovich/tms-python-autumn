# Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость(по
# умолчанию 0). Методы: увеличить скорости(скорость + 5), уменьшение
# скорости(скорость - 5), стоп(сброс скорости на 0), отображение скорости,
# разворот(изменение знака скорости). Все атрибуты приватные.

class Car:
    def __init__(self,  mark, model, year, speed = 0):
        self.__mark = mark
        self.__model = model
        self.__year = year
        self.__speed = speed

    def show_speed(self):
        print(self.__speed)

    def up_speed(self):
        if self.__speed < 0:
            self.__speed -= 5
        else:
            self.__speed +=5
    def down_speed(self):
        if self.__speed < 0:
            self.__speed += 5
        else:
            self.__speed -= 5

    def stop(self):
        self.__speed = 0

    def razvorot(self):
        self.__speed = -(self.__speed)

BMW = Car("BMW","X5", 2011)
BMW.up_speed()
BMW.show_speed()
BMW.razvorot()
BMW.up_speed()
BMW.show_speed()
