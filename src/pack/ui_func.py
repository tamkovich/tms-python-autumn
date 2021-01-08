from pack.classes import Math
from pack.exception import get_valid_float_argument
from pack.exception import get_valid_str_sign


def menu():
    while True:
        print("enter first argument: ")
        a = get_valid_float_argument()
        print("enter second argument: ")
        b = get_valid_float_argument()
        calculator = {
            "+": Math.sum_of_arg(a, b),
            "-": Math.subtraction_of_arg(a, b),
            "*": Math.mult_of_arg(a, b),
            "/": Math.division_of_arg(a, b),
        }
        print("enter sign")
        sign = get_valid_str_sign()
        result = calculator[sign]
        print(f"result = {result}")
        if (
            input(
                "\nenter 1 -- calculate again \n "
                "else    -- close\n your choise : "
            ) != "1"
        ):
            break
