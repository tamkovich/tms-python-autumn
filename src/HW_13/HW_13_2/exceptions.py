"""Выполнить задание 1 с использованием класса Math. Класс принимает в
качестве аргументов два числа. Определить 4 метода(сложение,
вычитание, умножение, деление). Добавить валидацию входных данных.
Программа должна состоять из четырех файлов(main.py, classes.py,
ui_func.py exceptions.py)"""


def first_exception():
    while True:
        a = input()
        try:
            a = float(a)
        except (ValueError):
            print("Bad input, try again! ")
        else:
            return a


def second_exception():
    while True:
        a = input()
        if a.isdigit():
            a = float(a)
            return a
        else:
            print("Bad input, try again!")
            continue
