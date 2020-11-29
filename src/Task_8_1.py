"""Описать функцию fact2( n ), вычисляющую двойной факториал :n!! =
1·3·5·...·n, если n — нечетное; n!! = 2·4·6·...·n, если n — четное (n > 0 —
параметр целого типа. С помощью этой функции найти двойные
факториалы пяти данных целых чисел"""

def double_fact(x):
    """Функция вычисляет двойной факториал числа"""
    if x % 2 == 0:
        fact = 0
        for i in range(1, x+1):
            if i % 2 == 0:
                fact += i
        print(fact)
    else:
        fact = 0
        for i in range(1, x+1):
            if i % 2 != 0:
                fact += i
        print(fact)

double_fact(3)
double_fact(4)
double_fact(5)
double_fact(6)
