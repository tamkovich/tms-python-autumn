""" Написать программу, в которой вводятся два операнда Х и Y и знак операции
sign (+, –, /, *). Вычислить результат Z в зависимости от знака. Предусмотреть
реакции на возможный неверный знак операции, а также на ввод Y=0 при
делении. Организовать возможность многократных вычислений без перезагрузки
программа (т.е. построить бесконечный цикл). В качестве символа прекращения
вычислений принять ‘0’ (т.е. sign='0')."""

while True:
    sign = input("Input operation: ")
    if sign == '0':
        break
    if sign in ("+", "-", "*", "/"):
        x = float(input("Input X: "))
        y = float(input("Input y: "))
        if sign == "+":
            print(x + y)
        elif sign == "-":
            print(x - y)
        elif sign == "*":
            print(x * y)
        else:
            if y == 0:
                print("Don't divide with zero")
            else:
                print(x / y)
    else:
        print("Not correct operation, input one more time")
