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
            print("На входе 3 значения")
            self.hours = args[0]
            self.minutes = args[1]
            self.seconds = args[2]
        elif args == ():
            print("Нет входных параметров")
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
        elif type(args[0]) is str:
            print(f"На входе 1 значение в виде строки: {args[0]}")
            arr = args[0].split('-')
            self.hours = int(arr[0])
            self.minutes = int(arr[1])
            self.seconds = int(arr[2])
        elif type(args[0]) is MyTime:
            print("На входе 1 значение в виде MyTime")
            copy_time = args[0]
            self.hours = copy_time.hours
            self.minutes = copy_time.minutes
            self.seconds = copy_time.seconds

        if self.seconds > 59:
            self.seconds -= 60
            self.minutes += 1
        if self.minutes > 59:
            self.minutes -= 60
            self.hours += 1
        if self.hours > 23:
            self.hours -= 24
        if self.hours < 0:
            self.hours = 0
        if self.minutes < 0:
            self.minutes = 0
        if self.seconds < 0:
            self.seconds = 0



    @property
    def time_in_seconds(self):
        return self.seconds + self.minutes * 60 + self.hours * 3600


    def show_time(self):
        res = f"Часы {self.hours}, минуты {self.minutes}, секунды {self.seconds}"
        return res

    def __lt__(self, other_time: 'MyTime') -> bool:
        return self.time_in_seconds < other_time.time_in_seconds

    def __gt__(self, other_time: 'MyTime') -> bool:
        return self.time_in_seconds > other_time.time_in_seconds

    def __eq__(self, other_time: 'MyTime') -> bool:
        return self.time_in_seconds == other_time.time_in_seconds

    def __ne__(self, other_time: 'MyTime') -> bool:
        return self.time_in_seconds != other_time.time_in_seconds

    def __le__(self, other_time: 'MyTime') -> bool:
        return self.time_in_seconds <= other_time.time_in_seconds

    def __ge__(self, other_time: 'MyTime') -> bool:
        return self.time_in_seconds >= other_time.time_in_seconds

time = MyTime(30,30,30)
print(time.show_time())




