"""Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость(по
умолчанию 0). Методы: увеличить скорости(скорость + 5), уменьшение
скорости(скорость - 5), стоп(сброс скорости на 0), отображение скорости,
разворот(изменение знака скорости). Все атрибуты приватные."""

class Car:
    def __init__(self, brand, model, year, velocity = 0):
        self.brand = brand
        self.model = model
        self.year = year
        self.velocity = velocity

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand

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

    @property
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def velocity(self, velocity):
        self.__velocity = velocity

    def increase_a_speed(self, velocity):
        return f" velocity is {velocity + 5}"

    def slow_a_speed(self, velocity):
        return f" velocity is {velocity - 5}"

    def stop(self,velocity):
        velocity = 0
        return velocity

    def print_velocity(self, velocity):
        return f"Velocity is{velocity}"

    def reversal(self, velocity):
        return f"Direction of speed{velocity * -1}"
