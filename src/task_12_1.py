"""Создать класс MyTime. Атрибуты: hours, minutes, seconds. Методы:
переопределить магические методы сравнения(==, !=, >=, <=, <, >),
сложения, вычитания, умножения на число, вывод на экран. Перегрузить
конструктор на обработку входных параметров вида: одна строка, три
числа, другой объект класса MyTime, и отсутствие входных параметров.
Реализовать нормальное отображение времени(​ 12:65:83​ - 13:06:23)
[my-oop-02] ​ Задание доделать в рамках cw12"""
# __lt__(self, other) - x < y вызывает x.__lt__(y).
# __le__(self, other) - x ≤ y вызывает x.__le__(y).
# __eq__(self, other) - x == y вызывает x.__eq__(y).
# __ne__(self, other) - x != y вызывает x.__ne__(y)
# __gt__(self, other) - x > y вызывает x.__gt__(y).
# __ge__(self, other) - x ≥ y вызывает x.__ge__(y).
import time


class MyTime:
    def __init__(self, *args, **kwargs):
        if len(args) == 0:
            print("Нет входных значений")
        elif len(args) == 3:
            print("На входе 3 значения")
            self.hours = args[0]
            self.minutes = args[1]
            self.seconds = args[2]
        elif type(args[0]) is str:
            print("На входе значение в виде строки")
            arr = args[0].split("-")
            self.hours = int(arr[0])
            self.minutes = int(arr[1])
            self.seconds = int(arr[2])
        elif type(args[0]) is MyTime:
            print("На входе 1 значение в виде MyTime")
            copy_time = args[0]
            self.hours = copy_time.hours
            self.minutes = copy_time.minutes
            self.seconds = copy_time.seconds

    @property
    def time_in_seconds(self):
        return self.seconds + self.minutes * 60 + self.hours * 3600

    def __lt__(self, other_time: "MyTime"):
        return self.time_in_seconds < other_time.time_in_seconds

    def __le__(self, other_time: "MyTime"):
        return self.time_in_seconds <= other_time.time_in_seconds

    def __eq__(self, other_time: "MyTime"):
        return self.time_in_seconds == other_time.time_in_seconds

    def __ne__(self, other_time: "MyTime"):
        return self.time_in_seconds != other_time.time_in_seconds

    def __gt__(self, other_time: "MyTime"):
        return self.time_in_seconds > other_time.time_in_seconds

    def __ge__(self, other_time: "MyTime"):
        return self.time_in_seconds >= other_time.time_in_seconds

    def __str__(self):
        return time.strftime("%H:%M:%S", time.gmtime(self.time_in_seconds))


time1 = MyTime(10, 30, 30)
time2 = MyTime(10, 00, 00)
time3 = MyTime("10-30-30")
time4 = MyTime(10, 68, 00)
time5 = MyTime(time2)
time5 = MyTime()

print(time2 < time1)
print(time2 == time1)
print(time2 != time1)
print(time2 > time1)
print(time2 >= time1)
print(time2 < time1)
print(time2 <= time1)
print(time4)
