"""Написать программу, в которой вводятся два операнда Х и Y и знак
операции sign (+, –, /, *).Вычислить результат Z в зависимости от знака.
Предусмотреть реакции на возможный неверный знак операции,а также на
ввод Y=0 при делении. Организовать возможность многократных вычислений без
перезагрузки программа(т.е. построить бесконечный цикл). В качестве
символа прекращения вычислений принять ‘0’ (т.е. sign='0')."""
while True:
    flag = True
    while True:
        X = input("input X: ")
        if X.isdigit():
            X = int(X)
            break
        else:
            print("input X again: ")
    while True:
        Y = input("input Y: ")
        if Y.isdigit():
            Y = int(Y)
            break
        else:
            print("input Y again: ")

    while True:
        sign = input("input sign: ")
        if sign == "+":
            Z = X + Y
            print(f"X + Y = {Z}")
        elif sign == "-":
            Z = X - Y
            print(f"X - Y = {Z}")
        elif sign == "/":
            if Y == 0:
                print("Y = 0, you cannot divide by zero, enter another sign: ")
                continue
            else:
                Z = float(X) / float(Y)
                print(f"X / Y = {Z}")
        elif sign == "*":
            Z = X * Y
            print(f"X * Y = {Z}")
        elif sign == "0":
            flag = False
            break
        else:
            print("input sign again: ")
    if not flag:
        break
