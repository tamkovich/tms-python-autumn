"""Создать пять классов описывающие реальные объекты. Каждый класс
должен содержать минимум три приватных атрибута, конструктор, геттеры
и сеттеры для каждого атрибута, два метода."""

class Pet:
    def __init__(self, master, name, color, weight):
        self.__master = master
        self.__color = color
        self.__weight = weight
        self.__name = name

    @property
    def master(self):
        return self.__master

    @master.setter
    def master(self, master):
        self.__master = master

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    def pat_pet(self):
        print(f'You have patted the {self.__name}')

    def feed_pet(self):
        print(f'You have feeded the {self.__name}')


class Cat(Pet):
    pass


class Dog(Pet):
    pass


class Parrot(Pet):
    pass


parrot1 = Parrot("Dima", "Talky", "Rainbow", "1")
parrot1.feed_pet()
