from classes import Math
from exceptions import get_valid_int_number


def calculator():
    while True:
        print('Put integer here: ')
        a = get_valid_int_number()
        print('Put anither integer: ')
        b = get_valid_int_number()
        symbol = input('Put sign (+, -, *, /) or put 0 for exit: ')
        math = Math(a, b)

        if symbol == "+":
            total1 = math.total
            print(f'Summary of numbers is: {total1}')

        elif symbol == "-":
            subtr1 = math.subtraction
            print(f'Subtraction of numbers is: {subtr1}')

        elif symbol == "*":
            mult1 = math.multiplication
            print(f'Mult. of numbers is : {mult1}')

        elif symbol == "/":
            if b != 0:
                div1 = math.dvzn
                print(f"Div. of numbers is: {div1}")
            else:
                print('Please enter second value other than zero')

        elif symbol == "0":
            print('End.')
            break

        else:
            print('Wrong input.')
