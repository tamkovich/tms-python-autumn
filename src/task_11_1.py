#Создать пять классов описывающие реальные объекты. Каждый класс
#должен содержать минимум три приватных атрибута, конструктор, геттеры
#и сеттеры для каждого атрибута, два метода.

class Animal:
    def __init__(self, name, age, height):
        self.__name = name
        self.__age = age
        self.__height = height

    def change_height(self, height):
        self.__height = height

    def change_name(self,name):
        self.__name = name

    def change_age(self,age):
        self.__age = age

    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.__height


    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        if len(name) < 5:
            self.__name = name

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        self.__name = age

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, height):
        self.__height = height


class Elephant(Animal):
    pass

class Crocodile(Animal):
    pass

class Lion(Animal):
    pass

lion_1 = Lion("Mark",12,187)
print(lion_1.name)
print(lion_1.age)
print(lion_1.height)
lion_1.change_name("Olaf")
lion_1.change_age(14)
lion_1.change_height(192)
print(lion_1.name)
print(lion_1.age)
print(lion_1.height)
lion_1.set_name("Patrick")
lion_1.set_age(16)
lion_1.set_height(198)
print(lion_1.get_name())
print(lion_1.get_age())
print(lion_1.get_height())