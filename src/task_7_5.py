def in_arg(*args):
    """Sum of multiplication.

    :param args:
    :return: summs: sum of multiplication between value and its index
    """
    summs = 0
    for index, value in enumerate(args):
        summs += index * value
    return summs


print(in_arg(1, 10, 3))
