# Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость(по
# умолчанию 0). Методы: увеличить скорости(скорость + 5), уменьшение
# скорости(скорость - 5), стоп(сброс скорости на 0), отображение скорости,
# разворот(изменение знака скорости). Все атрибуты приватные.


class Car:
    def __init__(self, brand, model, year, speed=0):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = speed
        # MAKE ALL PRIVAT

    @property
    def up_speed(self):
        self.__speed += 5
        return self.__speed

    @property
    def down_speed(self):
        self.__speed -= 5
        return self.__speed

    @property
    def stop(self):
        self.__speed = 0
        return self.__speed

    @property
    def speed_display(self):
        return self.__speed

    @property
    def revers(self):
        self.__speed = - self.__speed
        return self.__speed


Audi = Car("Audi", "A4", "2004", 120)
print(Audi.up_speed)
print(Audi.down_speed)
print(Audi.stop)
print(Audi.up_speed)
print(Audi.speed_display)
print(Audi.revers)
print("=====")
BMW = Car("BMW", "M3", "2009")
print(BMW.up_speed)
print(BMW.revers)
print(BMW.down_speed)
