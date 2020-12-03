def fact2(n: int):
    """This function finds the double factorial

    :param n: some number
    """
    fact = 1
    if n % 2 == 0:
        for i in range(2, n + 1, 2):
            fact *= i
    else:
        for i in range(1, n + 1, 2):
            fact *= i

    print(f"double factorial = {fact}")


while True:
    number = input("enter number : ")
    if number.isdigit() and int(number) > 0:
        fact2(int(number))
        break
