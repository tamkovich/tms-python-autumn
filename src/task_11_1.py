# Создать пять классов описывающие реальные объекты. Каждый класс
# должен содержать минимум три приватных атрибута, конструктор, геттеры
# и сеттеры для каждого атрибута, два метода.


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    @property
    def brand(self):
        return self.brand

    @brand.setter
    def brand(self, brand):
        self.brand = brand

    @property
    def model(self):
        return self.model

    @model.setter
    def model(self, model):
        self.model = model

    @property
    def year(self):
        return self.year

    @year.setter
    def year(self, year):
        self.year = year

    def old_of_car(self):
        if self.year < 2015:
            return "Good car!"
        else:
            return "you are grandfather!"


class BMW(Car):
    pass


class Opel(Car):
    pass


class Audi(Car):
    pass

class Ford(Car):
    pass


Audi_1 = Car("Audi", "A3", 2015)
