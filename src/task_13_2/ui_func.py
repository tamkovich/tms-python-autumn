"""Выполнить задание 1 с использованием класса Math. Класс принимает в
качестве аргументов два числа. Определить 4 метода(сложение,
вычитание, умножение, деление). Добавить валидацию входных данных.
Программа должна состоять из четырех файлов(main.py, classes.py,
ui_func.py exceptions.py)."""

from exceptions import exception
from classes import Math


def calcul():
    while True:
        print("Введите целое число: ")
        a = exception()
        print("Введите целое число: ")
        b = exception()
        operation = input("Введите знак (+, -, *, /) или введите 0 для выхода: ")
        math = Math(a, b)

        if operation == "+":
            sum_ = math.summa()
            print(f"Сумма двух чисел равна: {sum_}")

        elif operation == "-":
            subtraction_ = math.subtraction()
            print(f"Разность двух чисел равна: {subtraction_}")

        elif operation == "*":
            multiplication_ = math.multiplication()
            print(f"Произведение двух чисел равно: {multiplication_}")

        elif operation == "/":
            if b != 0:
                division_ = math.division()
                print(f"Результат деления двух чисел равно: {division_}")
            else:
                print("Деление на '0' невозможно, ведите второе число не равное '0'")
                continue

        elif operation == "0":
            print("Конец работы программы!")
            break

        else:
            print("Введен неверный знак")
            continue