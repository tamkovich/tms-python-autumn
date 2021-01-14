"""Задан целочисленный массив. Определить количество
участков массива,
на котором элементы монотонно возрастают
(каждое следующее число
больше предыдущего). [02-4.1-ML27]"""

import random

s = 0
a = []
b = int(input())
for i in range(1, b + 1):
    x = random.randint(0, 1000)
    a.append(x)
for g in range(0, len(a) - 1):
    if (a[g - 1]) < a[g] and a[g] < a[g + 1]:
        s += 1
print(a)
print(s)
