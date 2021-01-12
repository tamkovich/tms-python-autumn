from exceptions import exception_
from func import division
from func import multiplication
from func import subtraction
from func import summa


def calc():
    while True:
        print("Введите целое число:")
        a = exception_()
        print("Введите целое число:")
        b = exception_()
        znak = input("Введите знак (+, -, *, /) или введите 0 для выхода: ")

        if znak == "+":
            sum_ = summa(a, b)
            print(f"Сумма двух чисел равна: {sum_}")

        elif znak == "-":
            subtraction_ = subtraction(a, b)
            print(f"Разность двух чисел равна: {subtraction_}")

        elif znak == "*":
            multiplication_ = multiplication(a, b)
            print(f"Произведение двух чисел равно: {multiplication_}")

        elif znak == "/":
            if b != 0:
                division_ = division(a, b)
                print(f"Результат деления двух чисел равно: {division_}")
            else:
                print("Введите второе значение не равное 0")
                continue

        elif znak == "0":
            print("Конец работы программы!")
            break

        else:
            print("Введен не верный знак")
