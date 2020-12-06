'''Создать класс MyTime. Атрибуты: hours, minutes, seconds. Методы:
переопределить магические методы сравнения(==, !=, >=, <=, <, >),
сложения, вычитания, умножения на число, вывод на экран. Перегрузить
конструктор на обработку входных параметров вида: одна строка, три
числа, другой объект класса MyTime, и отсутствие входных параметров.
Реализовать нормальное отображение времени(12:65:83 - 13:06:23)
[my-oop-02]'''


class MyTime:
    def __init__(self, *args):
        if len(args) == 3:
            self.hours = args[0]
            self.minutes = args[1]
            self.seconds = args[2]
        elif args[0] is str:
            arr = args[0].split('-')
            self.hours = int(arr[0])
            self.minutes = int(arr[1])
            self.seconds = int(arr[2])
        elif type(args[0]) is MyTime:
            copy_time = args[0]
            self.hours = copy_time.hours
            self.minutes = copy_time.minutes
            self.seconds = copy_time.seconds
        elif args == ():
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
        while True:
            if self.seconds > 59:
                self.seconds -= 60
                self.minutes += 1
                if self.minutes > 59:
                    self.minutes -= 60
                    self.hours += 1
                    if self.hours > 23:
                        self.hours -= 24

    @property
    def time_in_seconds(self):
        hours_time_in_seconds = self.hours * 3600
        minutes_time_in_seconds = self.minutes * 60
        return self.seconds + minutes_time_in_seconds + hours_time_in_seconds

    def __eq__(self, other: 'MyTime') -> bool:
        return self.time_in_seconds == other.time_in_seconds

    def __ne__(self, other: 'MyTime') -> bool:
        return self.time_in_seconds > other.time_in_seconds

    def __lt__(self, other: 'MyTime') -> bool:
        return self.time_in_seconds > other.time_in_seconds

    def __gt__(self, other: 'MyTime') -> bool:
        return self.time_in_seconds < other.time_in_seconds

    def __le__(self, other: 'MyTime') -> bool:
        return self.time_in_seconds >= other.time_in_seconds

    def __ge__(self, other: 'MyTime') -> bool:
        return self.time_in_seconds >= other.time_in_seconds

    def __add__(self, other: 'MyTime') -> bool:
        return self.time_in_seconds + other.time_in_seconds

    def __sub__(self, other: 'MyTime') -> bool:
        return self.time_in_seconds - other.time_in_seconds

    def __mul__(self, other: 'MyTime') -> bool:
        return self.time_in_seconds * other

    def show_results(self):
        return f'{self.hours}:{self.minutes}:{self.seconds}'
