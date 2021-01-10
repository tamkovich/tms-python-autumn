"""Написать калькулятор. Программа должна содержать 4 функции
принимающие два аргумента и возвращающие результаты сложения,
вычитания, умножения и деления. Реализовать пользовательский
интерфейс с бесконечным циклом. Добавить валидацию входных данных.
Программа должна состоять из четырех файлов(main.py, func.py, ui_func.py
exceptions.py). [my-oop-t05] """


def summa(a, b: float) -> float:
    return a + b


def mult(a, b: float) -> float:
    return a * b


def deduction(a, b: float) -> float:
    return a - b


def division(a, b: float) -> float:
    return a / b
