"""Создать пять классов описывающие реальные объекты.
Каждый класс должен содержать минимум три приватных
атрибута,конструктор, геттеры и сеттеры для каждого
атрибута, два метода."""


class Clock:
    def __init__(self, brand, cost, year):
        self.__brand = brand
        self.__cost = cost
        self.__year = year

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, cost):
        self.__cost = cost

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year

    def change_year(self, year):
        self.__year = year

    def change_brand(self, brand):
        if self.__brand == "rolex":
            self.__brand = brand


clock = Clock("role", "leather", "blue")
clock.change_brand("zenit")
print(clock.brand)
print(clock.cost)


class Electronic(Clock):
    def __init__(self, brand, cost, year, display, capacity):
        super().__init__(brand, cost, year)
        self.__display = display
        self.__capacity = capacity

    @property
    def display(self):
        return self.__display

    @display.setter
    def display(self, display):
        self.__display = display

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity):
        self.__capacity = capacity


new_clock = Electronic("noRolex", 1200, 2005, "sensor", 4200)
print(new_clock.display, new_clock.capacity)


class Person:
    def __init__(self, name, surname, number):
        self.__name = name
        self.__surname = surname
        self.__number = number

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        self.__number = number

    def change_number(self):
        if self.__number.startswith("+375"):
            print("country Belarus")
        else:
            print("country not Belarus")


pers = Person("Igor", "Chvyrov", "+375442309940")
pers.change_number()


class Student(Person):
    def __init__(self, scholarship, group, name, surname, number):
        self.__scholarship = scholarship
        self.__group = group
        super().__init__(name, surname, number)

    @property
    def scholarship(self):
        return self.__scholarship

    @scholarship.setter
    def scholarship(self, scholarship):
        self.__scholarship = scholarship

    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, group):
        self.__group = group

    def grant(self):
        if self.group == "01":
            print(self)


sudent = Student(105, "01", "dima", "asdf", "809092232")
sudent.change_number()
sudent.grant()
