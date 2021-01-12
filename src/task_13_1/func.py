"""Написать калькулятор. Программа должна содержать 4 функции
принимающие два аргумента и возвращающие результаты сложения,
вычитания, умножения и деления. Реализовать пользовательский
интерфейс с бесконечным циклом. Добавить валидацию входных данных.
Программа должна состоять из четырех файлов(main.py, func.py, ui_func.py
exceptions.py)."""


def summa(a: int, b: int) -> int:
    return a + b


def subtraction(a: int, b: int) -> int:
    return a - b


def multiplication(a: int, b: int) -> int:
    return a * b


def division(a: int, b: int) -> float:
    return a / b
