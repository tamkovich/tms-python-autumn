"""Написать калькулятор. Программа должна содержать 4 функции
принимающие два аргумента и возвращающие результаты сложения,
вычитания, умножения и деления. Реализовать пользовательский
интерфейс с бесконечным циклом. Добавить валидацию входных данных.
Программа должна состоять из четырех файлов(main.py, func.py, ui_func.py
exceptions.py)."""


def exception():
    while True:
        x = input()
        if x.isdigit():
            x = int(x)
            return x
        else:
            print('Введено не целое число, введите новое значение: ')
            continue
