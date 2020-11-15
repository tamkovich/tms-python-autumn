while True:
    X = int(input("vvedite X: "))
    Y = int(input("vvedite Y: "))
    sign = input("vvedite operaciu: ")
    if sign == "0":
        break
    elif sign == "+":
        Z = X + Y
        print(f"summa ishodnih chisel, {Z}")
    elif sign == "-":
        Z = X - Y
        print(f"rasnost' ishodnih chisel, {Z}")
    elif sign == "*":
        Z = X * Y
        print(f"proizvedenie ishodnih chisel, {Z}")
    elif sign == "/":
        if Y == 0:
            print("delenie na '0' nevozmojno!")
        else:
            Z = X / Y
            print(f"delenie ishodnih chisel, {Z}")
