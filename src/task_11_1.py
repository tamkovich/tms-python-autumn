"""Создать пять классов описывающие реальные объекты. Каждый класс
должен содержать минимум три приватных атрибута, конструктор, геттеры
и сеттеры для каждого атрибута, два метода."""

class Cars:
    def __init__(self, color, age, transmission):
        self.__color = color
        self.__age = age
        self.__transmission = transmission

    def get_color(self):
        return self.__color

    def get_age(self):
        return self.__age

    def get_transmission(self):
        return self.__transmission

    def set_color(self, color):
        self.__color = color

    def set_age(self, age):
        self.__age = age

    def set_transmission(self, transmission):
        self.__transmission = transmission

    @property
    def color(self):
        return self.__color

    @property
    def age(self):
        return self.__age

    @property
    def transmission(self):
        return self.__transmission

    @color.setter
    def color(self, color):
        self.__color = color

    @age.setter
    def age(self, age):
        self.__age = age

    @transmission.setter
    def transmission(self, transmission):
        self.__transmission = transmission


class Audi(Cars):
    pass


class VW(Cars):
    pass


class Honda(Cars):
    pass


class Ziguli(Cars):
    pass


f = Cars('green', 2017, 'mehanica')
civic = Honda('white', 2000, 'robot')
print(civic.color)
civic.color = 'yelow'
print(civic.color)
polo = VW('black', 2018, 'mt')
polo.color = 'orange'
print(polo.color)
polo.age = 2016
print(polo.age)
