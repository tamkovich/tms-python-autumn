"""Выполнить задание 1 с использованием класса Math. Класс принимает в
качестве аргументов два числа. Определить 4 метода(сложение,
вычитание, умножение, деление). Добавить валидацию входных данных.
Программа должна состоять из четырех файлов(main.py, classes.py,
ui_func.py exceptions.py)"""

from exceptions import first_exception
from exceptions import second_exception
from Classes import Math


def calculator():
    while True:
        print("Enter the first number: ")
        a = first_exception()
        print("Enter the second number: ")
        b = second_exception()
        operation = input("Choice step (+, -, *, /) 0 - stop: ")
        math = Math(a, b)

        if operation == "+":
            sum_ = math.summa()
            print(f"Summa: {sum_}")

        elif operation == "-":
            deduction_ = math.deduction()
            print(f"Substraction: { deduction_ }")

        elif operation == "*":
            mult_ = math.mult()
            print(f"mult : {mult_}")

        elif operation == "/":
            if b != 0:
                div_ = math.div()
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
