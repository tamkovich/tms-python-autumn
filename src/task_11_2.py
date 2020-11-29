#Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость(по
#умолчанию 0). Методы: увеличить скорости(скорость + 5), уменьшение
#скорости(скорость - 5), стоп(сброс скорости на 0), отображение скорости,
#разворот(изменение знака скорости). Все атрибуты приватные.

class Car():
    def __init__(self,brand,model,year,speed=0):  #задает значения
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = speed

    def increase_speed(self):  # увеличивает скорость на 5
        self.__speed += 5
    def reduce_speed(self):   # уменьшает скорость на 5
        self.__speed -= 5
    def stop_speed(self):   # устанавливает скорость на 0
        self.__speed = 0
    def show_speed(self):   # выводит на печать нынашнюю скорость
        print(self.__speed)
    def turn_over(self):    # обращает скорость к противоположному знаку
        self.__speed *= -1

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year


car_1 = Car("BMW","E34",1992,0)
print(car_1.brand)
car_1.increase_speed()
car_1.increase_speed()
car_1.increase_speed()
print(car_1.speed)
print(car_1.model)
print(car_1.year)

car_1.turn_over()
car_1.show_speed()
