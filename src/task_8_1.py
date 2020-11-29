# Описать функцию fact2( n ), вычисляющую двойной факториал :n!! =
# 1·3·5·...·n, если n — нечетное; n!! = 2·4·6·...·n, если n — четное (n > 0 —
# параметр целого типа. С помощью этой функции найти двойные
# факториалы пяти данных целых чисел

def fact2(n: int):
    fact1 = 1
    fact2 = 2
    for i in range(1, n-1):
        if n % 2 == 0 and i % 2 == 0:
            fact2 *= i + 2
        elif n % 2 != 0 and i % 2 != 0:
            fact1 *= i + 2
    if n % 2 == 0:
        return f'Факториал равен {fact2}'
    else:
        return f'Факториал равен {fact1}'


print(fact2(5))
print(fact2(6))
print(fact2(7))
print(fact2(8))
print(fact2(9))
