from .exceptions import get_valid_float_argument
from .exceptions import get_valid_str_sign
from .func import division_of_arg
from .func import mult_of_arg
from .func import subtraction_of_arg
from .func import sum_of_arg


def menu():
    while True:
        print("enter first argument ")
        a = get_valid_float_argument()
        print("enter second argument ")
        b = get_valid_float_argument()
        calculator = {
            "+": sum_of_arg(a, b),
            "-": subtraction_of_arg(a, b),
            "*": mult_of_arg(a, b),
            "/": division_of_arg(a, b),
        }
        while True:

            print("enter sign: ")
            sign = get_valid_str_sign()
            result = calculator[sign]
            print(result)
            if (
                input(
                    "\nenter 1 -- if you want to change sign of operation \n"
                    "else    -- back\n your choise :  "
                ) != "1"
            ):
                break

        if (
            input(
                "\nenter 1 -- if you want to change arguments \n "
                "else    -- close\n your choise : "
            ) != "1"
        ):
            break
