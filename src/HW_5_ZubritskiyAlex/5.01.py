#Написать программу, в которой вводятся два операнда Х и Y и знак операции
#sign (+, –, /, *). Вычислить результат Z в зависимости от знака. Предусмотреть
#реакции на возможный неверный знак операции, а также на ввод Y=0 при
#делении. Организовать возможность многократных вычислений без перезагрузки
#программа (т.е. построить бесконечный цикл). В качестве символа прекращения
#вычислений принять ‘0’ (т.е. sign='0').

while True:

    x = int(input())
    y = int(input())
    sign = input()

    if sign == "0":
        break
    elif sign != 0:

        if sign == "/":
            if y == 0:
                print("Zero division error")
                break
            else:
                print(x / y)

        elif sign == "*":
            print(x * y)
        elif sign == "+":
            print(x + y)
        elif sign == "-":
            print(x - y)
        elif sign != "/" or sign != "+" or sign != "-" or sign != "*":
            print("try again ")
