# Создать класс MyTime. Атрибуты: hours, minutes, seconds. Методы:
# переопределить магические методы сравнения(==, !=, >=, <=, <, >),
# сложения, вычитания, умножения на число, вывод на экран. Перегрузить
# конструктор на обработку входных параметров вида: одна строка, три
# числа, другой объект класса MyTime, и отсутствие входных параметров.
# Реализовать нормальное отображение времени (12:65:83 - 13:06:23)
import datetime


class MyTime:
    def __init__(self, *args):
        if len(args) == 3:
            print('На входе 3 значения')
            self.hours = args[0]
            self.minutes = args[1]
            self.seconds = args[2]

        elif type(args[0]) is str:
            print(f"На входе строка :{args[0]}")
            array = args[0].split('-')
            self.hours = int(array[0])
            self.minutes = int(array[1])
            self.seconds = int(array[2])

        elif type(args[0]) is MyTime:
            print('На входе значения в виде MyTime:')
            copytime = args[0]
            self.hours = copytime.hours
            self.minutes = copytime.minutes
            self.seconds = copytime.seconds

        elif not args:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0

        if self.hours > 23 or self.minutes > 59 or self.seconds > 59:
            raise Exception('Введён неверный формат времени')

    def show_time(self):
        print(f"Time is {self.hours}: {self.minutes}: {self.seconds}")

    @property
    def time_in_seconds(self):
        return self.seconds + self.minutes * 60 + self.hours * 3600

    def __lt__(self, other_time: 'MyTime') -> bool:
        return self.time_in_seconds < other_time.time_in_seconds

    def __gt__(self, other_time: 'MyTime') -> bool:
        return self.time_in_seconds > other_time.time_in_seconds

    def __ge__(self, other_time: 'MyTime') -> bool:
        return self.time_in_seconds >= other_time.time_in_seconds

    def __le__(self, other_time: 'MyTime') -> bool:
        return self.time_in_seconds <= other_time.time_in_seconds

    def __eq__(self, other_time: 'MyTime') -> bool:
        return self.time_in_seconds == other_time.time_in_seconds

    def __ne__(self, other_time: 'MyTime') -> bool:
        return self.time_in_seconds != other_time.time_in_seconds

    def __add__(self, other_time: 'MyTime') -> int:
        return self.time_in_seconds + other_time.time_in_seconds

    def __sub__(self, other_time: 'MyTime') -> int:
        return self.time_in_seconds - other_time.time_in_seconds

    def __mul__(self, other_time: 'MyTime') -> int:
        return self.time_in_seconds * other_time.time_in_seconds


time1 = MyTime('12 - 30 - 33')
time1.show_time()
time2 = MyTime(time1)
time2.show_time()
print(datetime.timedelta(seconds=time1.time_in_seconds))
print(datetime.timedelta(seconds=time1.__add__(time2)))
