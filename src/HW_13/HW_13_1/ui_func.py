"""Написать калькулятор. Программа должна содержать 4 функции
принимающие два аргумента и возвращающие результаты сложения,
вычитания, умножения и деления. Реализовать пользовательский
интерфейс с бесконечным циклом. Добавить валидацию входных данных.
Программа должна состоять из четырех файлов(main.py, func.py, ui_func.py
exceptions.py)."""

from exceptions import first_exception
from exceptions import second_exception
from func import division
from func import mult
from func import deduction
from func import summa


def calculator():
    while True:
        print("Enter the first number: ")
        a = first_exception()
        print("Enter the second number: ")
        b = second_exception()
        operation = input("Choice step (+, -, *, /) 0 - stop: ")

        if operation == "+":
            sum_ = summa(a, b)
            print(f"Summa: {sum_}")

        elif operation == "-":
            deduction_ = deduction(a, b)
            print(f"Substraction: { deduction_ }")

        elif operation == "*":
            mult_ = mult(a, b)
            print(f"mult : {mult_}")

        elif operation == "/":
            if b != 0:
                div_ = division(a, b)
                print(f" result of division: {div_}")
            else:
                print("Zero divizion error, try again!")
                continue

        elif operation == "0":
            print("The end")
            break

        else:
            print("Bad symbol, try again!")
            continue
