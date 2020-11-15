# Создать пять классов описывающие реальные объекты. Каждый класс
# должен содержать минимум три приватных атрибута, конструктор, геттеры
# и сеттеры для каждого атрибута, два метода.
class Pet:
    def __init__(self,  name, age, weight):
        self.__name = name
        self.__age = age
        self.__weight = weight

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    def wash(self):
        print(f'Я мою {self.__name}')

    def sleep(self):
        print(f'{self.__name} ZzzZzzzzz')

class Cat(Pet):
    pass

class Dog(Pet):
    pass

class Parrot(Pet):
    pass

parrot1 = Parrot("Vlados", 51, "140")
parrot1.wash()