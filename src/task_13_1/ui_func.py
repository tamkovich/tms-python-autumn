"""Написать калькулятор. Программа должна содержать 4 функции
принимающие два аргумента и возвращающие результаты сложения,
вычитания, умножения и деления. Реализовать пользовательский
интерфейс с бесконечным циклом. Добавить валидацию входных данных.
Программа должна состоять из четырех файлов(main.py, func.py, ui_func.py
exceptions.py)."""

from exceptions import exception
from func import division
from func import multiplication
from func import subtraction
from func import summa


def calcul():
    while True:
        print("Введите целое число: ")
        a = exception()
        print("Введите целое число: ")
        b = exception()
        operation = input("Введите знак (+, -, *, /) или введите 0 для выхода: ")

        if operation == "+":
            sum_ = summa(a, b)
            print(f"Сумма двух чисел равна: {sum_}")

        elif operation == "-":
            subtraction_ = subtraction(a, b)
            print(f"Разность двух чисел равна: {subtraction_}")

        elif operation == "*":
            multiplication_ = multiplication(a, b)
            print(f"Произведение двух чисел равно: {multiplication_}")

        elif operation == "/":
            if b != 0:
                division_ = division(a, b)
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
