while True:
    sign = input("введите знак операции (+, -, *, /): ")
    if sign == "0":
        print("Операция прекращена")
        break
    if sign in ("+", "-", "*", "/"):
        x = float(input("Введите X: "))
        y = float(input("Введите y: "))
        if sign == "+":
            print(x + y)
        elif sign == "-":
            print(x - y)
        elif sign == "*":
            print(x * y)
        elif sign == "/":
            print(x / y)
    else:
        print("ВВеден не правильный знак операции")
