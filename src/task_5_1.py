"""Написать программу, в которой вводятся
два операнда Х и Y и знак операции
sign (+, –, /, *). Вычислить результат Z в
зависимости от знака. Предусмотреть
реакции на возможный неверный знак операции,
а также на ввод Y=0 при
делении. Организовать возможность многократных
вычислений без перезагрузки
программа (т.е. построить бесконечный цикл). В
качестве символа прекращения
вычислений принять ‘0’ (т.е. sign='0')."""


a = ("+", "-", "*", "/")
while True:
    print("Vvedite znak + , - , * , /, ili 0 dlia ostanovki rascheta")
    z = str(input())
    if z == "0":
        break
    if z in a:
        print("Vvedite 2 chisla")
        x = input()
        y = input()
        if x.isdigit() and y.isdigit():
            x = int(x)
            y = int(y)
        if z == "+":
            print(x + y)
        if z == "-":
            print(x - y)
        if z == "*":
            print(x * y)
        if z == "/":
            if y != 0:
                print(x / y)
            else:
                print("delenie nevozmozhno")
    else:
        print("Nevernii znak")
