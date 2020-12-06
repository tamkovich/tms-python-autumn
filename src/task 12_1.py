#Создать класс MyTime. Атрибуты: hours, minutes, seconds. Методы:
#переопределить магические методы сравнения(==, !=, >=, <=, <, >),
#сложения, вычитания, умножения на число, вывод на экран. Перегрузить
#конструктор на обработку входных параметров вида: одна строка, три
#числа, другой объект класса MyTime, и отсутствие входных параметров.
#Реализовать нормальное отображение времени(12:65:83 - 13:06:23)
#[my-oop-02] Задание доделать в рамках cw12
#Примечание: http://sheregeda.github.io/blog/2015/01/18/maghichieskiie-mietody-python/

import datetime
class MyTime:
    def __init__(self, *args, **kwargs):
        if len(args) == 3:
            print("На входе 3 значения")
            self.hours = args[0]
            self.minutes = args[1]
            self.seconds = args[2]
        elif type(args[0]) is str:
            print(f"На входе 1 значение в виде строки: {args[0]}")
            arr = args[0].split(':')
            self.hours = int(arr[0])
            self.minutes = int(arr[1])
            self.seconds = int(arr[2])
        elif type(args[0]) is MyTime:
            print("На входе 1 значение в виде MyTime")
            copy_time = args[0]
            self.hours = copy_time.hours
            self.minutes = copy_time.minutes
            self.seconds = copy_time.seconds
        elif not args:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
        if self.hours > 23 or self.minutes > 59 or self.seconds > 59:
            raise Exception("введен неправильный формат времени, аргументы не должны превышать 23:59:59")
    def show_time(self):
        print(f"время {self.hours}:{self.minutes}:{self.seconds}")

    @property
    def time_in_seconds(self):
        return self.seconds + self.minutes * 60 + self.hours * 3600

    def __eq__(self, other: 'MyTime') -> bool:
        return self.time_in_seconds == other.time_in_seconds
    def __lt__(self, other: 'MyTime'):
        return self.time_in_seconds < other.time_in_seconds
    def __len__(self, other: 'MyTime'):
        return self.time_in_seconds <= other.time_in_seconds
    def __ne__(self, other: 'MyTime'):
        return self.time_in_seconds != other.time_in_seconds
    def __gt__(self, other: 'MyTime'):
        return self.time_in_seconds > other.time_in_seconds
    def __ge__(self, other: 'MyTime'):
        return self.time_in_seconds >= other.time_in_seconds
    def __add__(self, other: 'MyTime'):
        return self.time_in_seconds + other.time_in_seconds
    def __sub__(self, other: 'MyTime'):
        return self.time_in_seconds - other.time_in_seconds
    def __mult__(self, other: 'MyTime'):
        return self.time_in_seconds * other.time_in_seconds

time = MyTime(15, 30, 59)
time.show_time()
time_2 = MyTime(time)
time_2.show_time()
print(datetime.timedelta(seconds = time.__add__(time_2)))
