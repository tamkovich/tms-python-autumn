def get_valid_float_argument() -> float:
    """Function checks for a number"""
    while True:
        some_argument = input("argument: ")
        if some_argument.replace('.', '', 1).isdigit():
            some_argument = float(some_argument)
            return some_argument
        else:
            print("enter argument again: ")


def get_valid_str_sign() -> str:
    """Function checks for the entered sign"""
    while True:
        a = input("sign: ")
        if a == "+" or a == "-" or a == "*" or a == "/":
            return a
        else:
            print("enter sign again: ")
