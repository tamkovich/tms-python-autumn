"""Написать калькулятор. Программа должна содержать 4 функции
принимающие два аргумента и возвращающие результаты сложения,
вычитания, умножения и деления. Реализовать пользовательский
интерфейс с бесконечным циклом. Добавить валидацию входных данных.
Программа должна состоять из четырех файлов(main.py, func.py, ui_func.py
exceptions.py)."""


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
