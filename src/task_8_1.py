# Описать функцию fact2( n ), вычисляющую двойной факториал :n!! =
# 1·3·5·...·n, если n — нечетное; n!! = 2·4·6·...·n, если n — четное (n > 0 —
# параметр целого типа. С помощью этой функции найти двойные
# факториалы пяти данных целых чисел


def fact2(n: int) -> int:
    """
    This method calculates double factorial

    :param n: integer
    :return: integer
    """
    if n % 2 == 0:
        factorial = 1
        even_list = []
        for i in range(2, n + 1, 2):
            even_list.append(i)
        for j in even_list:
            factorial = factorial * j
    if n % 2 != 0:
        factorial = 1
        odd_list = []
        for i in range(1, n + 1, 2):
            odd_list.append(i)
        for j in odd_list:
            factorial = factorial * j
    return factorial


print(fact2(7))
print(fact2(6))
print(fact2(1))
print(fact2(9))
print(fact2(3))
