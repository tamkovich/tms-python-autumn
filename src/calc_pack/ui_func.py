from exceptions import exc3ption
from func import total
from func import subtraction
from func import multiplication
from func import dvzn1312


def calculator():
    while True:
        print('Put integer here: ')
        a = exc3ption()
        print('Put other one here: ')
        b = exc3ption()
        symbol = input('Put sign (+, -, *, /) or put 0 for exit: ')

        if symbol == "+":
            total1 = total(a, b)
            print(f"Summary of digits is: {total1}")

        elif symbol == "-":
            subtr1 = subtraction(a, b)
            print(f"Subtraction of digits is: {subtr1}")

        elif symbol == "*":
            mult1 = multiplication(a, b)
            print(f"Multiplication if digits is: {mult1}")

        elif symbol == "/":
            if b != 0:
                div1 = dvzn1312(a, b)
                print(f"Division of digits is: {div1}")
            else:
                print('Please enter second value other than zero')
                continue

        elif symbol == "0":
            print("End.")
            break

        else:
            print("Wrong input.")
            continue
