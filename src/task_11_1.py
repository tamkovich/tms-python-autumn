# Создать пять классов описывающие реальные объекты. Каждый класс
# должен содержать минимум три приватных атрибута, конструктор, геттеры
# и сеттеры для каждого атрибута, два метода.

class Horse:
    def __init__(self, name, age, height):
        self.__name = name
        self.__age = age
        self.__height = height

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_height(self):
        return self.__height

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_height(self, height):
        self.__height = height

    def voice_horse(self):
        print('и-го-го!')

    def eat_horse(self):
        print('Grass')


class Dog:
    def __init__(self, name, age, height):
        self.__name = name
        self.__age = age
        self.__height = height

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_height(self):
        return self.__height

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_height(self, height):
        self.__height = height

    def voice_dog(self):
        print('гав-гав!')

    def eat_dog(self):
        print('Bones')


class Cat:
    def __init__(self, name, age, height):
        self.__name = name
        self.__age = age
        self.__height = height

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_height(self):
        return self.__height

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_height(self, height):
        self.__height = height

    def voice_cat(self):
        print('мяу-мяу!')

    def eat_cat(self):
        print('Milk')


class Wolf:
    def __init__(self, name, age, height):
        self.__name = name
        self.__age = age
        self.__height = height

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_height(self):
        return self.__height

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_height(self, height):
        self.__height = height

    def voice_wolf(self):
        print('воет на луну')

    def eat_wolf(self):
        print('Meat')


class Rat:
    def __init__(self, name, age, height):
        self.__name = name
        self.__age = age
        self.__height = height

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_height(self):
        return self.__height

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_height(self, height):
        self.__height = height

    def voice_rat(self):
        print('шуршит')

    def eat_rat(self):
        print('Cheese')
