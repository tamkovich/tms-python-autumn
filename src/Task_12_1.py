""". Создать класс MyTime. Атрибуты: hours, minutes, seconds. Методы:
переопределить магические методы сравнения(==, !=, >=, <=, <, >),
сложения, вычитания, умножения на число, вывод на экран. Перегрузить
конструктор на обработку входных параметров вида: одна строка, три
числа, другой объект класса MyTime, и отсутствие входных параметров.
Реализовать нормальное отображение времени"""


import datetime

class MyTime:
    def __init__(self, *args):
        if len(args) == 3:
            self.hours = args[0]
            self.minutes = args[1]
            self.seconds = args[2]
        elif type(args[0]) is str:
            x = args[0].split(";")
            self.hours = int(x[0])
            self.minutes = int(x[1])
            self.seconds = int(x[2])
        elif type(args[0]) is MyTime:
            fake_time = args[0]
            self.hours = fake_time.hours
            self.minutes = fake_time.minutes
            self.seconds = fake_time.seconds
        elif not args:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0

        if self.hours > 23 or self.minutes > 60 or self.seconds > 60:
            raise Exception("Введено неправильное время")

    def show_time(self):
        print(f'Время: {self.hours}:{self.minutes}:{self.seconds}')

    @property
    def time_in_seconds(self):
        return self.seconds + self.minutes * 60 + self.hours * 3600

    def __eq__(self, other: 'MyTime') -> bool:
        return self.time_in_seconds == other.time_in_seconds

    def __lt__(self, other: 'MyTime'):
        return self.time_in_seconds < other.time_in_seconds

    def __le__(self, other: 'MyTime'):
        return self.time_in_seconds <= other.time_in_seconds

    def __ne__(self, other: 'MyTime'):
        return self.time_in_seconds != other.time_in_seconds

    def __gt__(self, other: 'MyTime'):
        return self.time_in_seconds > other.time_in_seconds

    def __ge__(self, other: 'MyTime'):
        return self.time_in_seconds >= other.time_in_seconds

    def __add__(self, other: 'MyTime') -> int:
        return self.time_in_seconds + other.time_in_seconds

    def __sub__(self, other: 'MyTime') -> int:
        return self.time_in_seconds - other.time_in_seconds

    def __mul__(self, other: 'MyTime') -> int:
        return self.time_in_seconds * other.time_in_seconds


time1 = MyTime(12, 45, 30)
time1.show_time()
time2 = MyTime(time1)
time2.show_time()
print(datetime.timedelta(seconds=time1.time_in_seconds))
print(datetime.timedelta(seconds=time1.__add__(time2)))
