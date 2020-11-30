"""Описать функцию fact2( n ), вычисляющую двойной факториал :n!! =
1·3·5·...·n, если n — нечетное; n!! = 2·4·6·...·n, если n — четное (n > 0 —
параметр целого типа. С помощью этой функции найти двойные
факториалы пяти данных целых чисел"""

numbers=int(input('vvedite chislo N: '))


def fact2(n):
    m = 1
    if n % 2 == 0:
        for i in range(n, 1, -2):
            print(i)
            m *= i
    else:
        for i in range(1, n + 1, 2):
            print(i)
            m *= i
    return m

x = fact2(numbers)
print(f'Dvoinoi factorial vvedennogo chisla {numbers}:', x)
