# Описать функцию fact2( n ), вычисляющую двойной факториал :n!! =
# 1·3·5·...·n, если n — нечетное; n!! = 2·4·6·...·n, если n — четное (n > 0 —
# параметр целого типа. С помощью этой функции найти двойные
# факториалы пяти данных целых чисел"""
# функия вычисления двойного факториала числа
def d2_factorial(x):
    if x % 2 == 0:
        factorial = 2
        for i in range(1, x + 1):
            if i % 2 == 0:
                factorial *= i
        print(factorial)
    else:
        factorial = 1
        for i in range(1, x + 1):
            if i % 2 != 0:
                factorial *= i
        print(factorial)

d2_factorial(5)
d2_factorial(6)
d2_factorial(7)
d2_factorial(8)