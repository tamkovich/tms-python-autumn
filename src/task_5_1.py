a = ("+", "-", "*", "/")
while True:
    print("Vvedite znak + , - , * , /, ili 0 dlia ostanovki rascheta")
    z = str(input())
    if z == "0":
        break
    if z in a:
        print("Vvedite 2 chisla")
        x = float(input())
        y = float(input())
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
