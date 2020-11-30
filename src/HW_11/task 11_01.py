"""Создать пять классов описывающие реальные объекты. Каждый класс
должен содержать минимум три приватных атрибута, конструктор, геттеры
и сеттеры для каждого атрибута, два метода."""
class Ihar:
        def __init__(self, name, age, size,phone_number):
            self.name = name
            self.age = age
            self.size = size
            self.phone_number = phone_number

        def eat(self):
            return "Ihar is eat"

        def sleep(self):
            return "Ihar is sleeping"

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
        def size(self):
            return self.__size

        @size.setter
        def size(self, size):
            self.__size = size

        @property
        def phone_number(self):
            return self.__phone_number

        @phone_number.setter
        def phone_number(self, phone_number):
            self.__phone_number = phone_number

class Book:
    def __init__(self, name_of_keeper, year, size, adres_of_library):
        self.name_of_keeper = name_of_keeper
        self.year = year
        self.size = size
        self.adress_of_library = adres_of_library


    def delete_page(self):
        self.size -= 1
        return self.size

    def change_name_of_keeper(self):
        new_keeper = input("Enter the name")
        self.name_of_keeper = new_keeper
        return new_keeper

    @property
    def name_of_keeper(self):
        return self.__name_of_keeper

    @name_of_keeper.setter
    def name_of_keeper(self, name_of_keeper):
        self.__name_of_keeper = name_of_keeper

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year

    @property
    def adress_of_library(self):
        return self.__adress_of_library

    @adress_of_library.setter
    def adress_of_library(self, adress_of_library):
        self.__adress_of_library = adress_of_library



class Motorcycle:
    def __init__(self, brand, year, max_velocity):
        self.brand = brand
        self.year = year
        self.max_velocity = max_velocity

    def start_drive(self):
        return "Wrooooooooooooooom!"

    def stop_drive(self):
        return  "STOP!"

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

    def get_max_velocity(self):
        return self.__max_velocity

    def set_max_velocity(self, max_velocity):
        self.__max_velocity = max_velocity

class ShoppingCenter:

    def __init__(self, floor, total_money_in_center, list_of_shops):
        self.floor = floor
        self.total_money_in_center = total_money_in_center
        self.list_of_shops = list_of_shops

    def change_floor(self,floor):
        return f"You are on the{floor}th floor"

    def converte_total_money_in_center(self,total_money_in_center):
        return f"{total_money_in_center/2.59} USD\n {total_money_in_center/3.10} EURO\n"

    def list_of_shops(self,list_of_shops):
        return f" Our shopping center has the following stories:\n{list_of_shops}"

    def get_floor(self):
        return self.__floor

    def set_floor(self, floor):
        self.__floor = floor

    def get_total_money_in_center(self):
        return self.__total_money_in_center

    def set_total_money_in_center(self, total_money_in_center):
        self.__total_money_in_center = total_money_in_center

    def get_list_of_shops(self):
        return self.__list_of_shops

    def set_list_of_shops(self, list_of_shops):
        self.__list_of_shops = list_of_shops


class House:
    def __init__(self, living_sqare, amount_of_room, adress_of_house):
        self.living_sqare = living_sqare
        self.amount_of_room = amount_of_room
        self.adress_of_house = adress_of_house

    @property
    def living_sqare(self):
        return self.__living_sqare

    @living_sqare.setter
    def living_sqare(self, living_sqare):
        self.__living_sqare = living_sqare

    @property
    def amount_of_room(self):
        return self.__amount_of_room

    @amount_of_room.setter
    def amount_of_room(self, amount_of_room):
        self.__amount_of_room = amount_of_room

    @property
    def adress_of_house(self):
        return self.__adress_of_house

    @adress_of_house.setter
    def adress_of_house(self, adress_of_house):
        self.__adress_of_house = adress_of_house

    def location(self, adress_of_house):
        return f"This house is located {adress_of_house}"

    def add_room(self, amount_of_room):
        return f" New room added, amount of room: {amount_of_room + 1 }"






