"""Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость(по
умолчанию 0). Методы: увеличить скорости(скорость + 5), уменьшение
скорости(скорость - 5), стоп(сброс скорости на 0), отображение скорости,
разворот(изменение знака скорости). Все атрибуты приватные."""

class Cars:
    def __init__(self, marka, model, year, speed=0):
        self.__marka = marka
        self.__model = model
        self.__year = year
        self.__speed = speed

    def increase_speed(self):
        self.__speed += 5

    def decrease_speed(self):
        self.__speed -= 5

    def reset_speed(self):
        self.__speed = 0

    def reverse_speed(self):
        self.__speed = - self.__speed

    @property
    def speed(self):
        return self.__speed

    @property
    def year(self):
        return self.__year


honda = Cars('Honda', 'Civic', 2004)
print(honda.speed)
honda.increase_speed()
print(honda.speed)
honda.reverse_speed()
honda.decrease_speed()
print(honda.speed)
honda.reset_speed()
print(honda.speed)
