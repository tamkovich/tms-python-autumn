from exception import exceptn
from func import sum
from func import sub
from func import mult
from func import div


def calculator():
    while True:
        print('Введите число')
        a = exceptn()
        print('Введите число ')
        b = exceptn()
        operation = input('Введите знак операции: (+, -, *, /) или введите "00" для выхода ')

        if operation == "+":
            sum1 = sum(a, b)
            print(f"Сумма чисел: {sum1}")

        elif operation == "-":
            sub1 = sub(a, b)
            print(f"Разница чисел: {sub1}")

        elif operation == "*":
            mult1 = mult(a, b)
            print(f"Произведение чисел: {mult1}")

        elif operation == "/":
            if b != 0:
                div1 = div(a, b)
                print(f"Частное от деления: {div1}")
            else:
                print('На ноль делить нельзя')
                continue

        elif operation == "00":
            print("Вы ввели команду выхода 00")
            break

        else:
            print("Введите числовое значение")
            continue
