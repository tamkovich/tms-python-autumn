class Car:
    def __init__(self, name, model, year, speed):
        self.__name = name
        self.__model = model
        self.__year = year
        self.speed = speed

    def plus_speed(self, speed = 5):
        self.speed +=speed

    def minus_speed(self, speed = -5):
        self.speed +=speed

    def stop(self, speed = 0):
        self.speed = 0

    def speedometer(self):
        print(self.speed)

    def razvorot(self):
        self.speed = (-self.speed)

tachka = Car('boomer', 'z3', 2007, 0)

tachka.plus_speed()
tachka.plus_speed()
tachka.speedometer()
tachka.minus_speed()
tachka.minus_speed()
tachka.minus_speed()
tachka.minus_speed()
tachka.minus_speed()
tachka.minus_speed()
tachka.speedometer()
tachka.razvorot()
tachka.speedometer()
tachka.stop()
tachka.speedometer()
