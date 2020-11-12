"""Дана целочисленная квадратная матрица. Найти в каждой строке наибольший элемент и поменять его местами с элементом главной диагонали.
"""

import random
n = int(input("Input number of element in 1st row"))
arr = [[random.randint(1, 100) for i in range(n)] for j in range(n)]
for i in arr:
    print(i, end='\n')
for row in arr:
    value = max(row)
    place = row.index(value)
    if place != arr.index(row):
        row[place], row[arr.index(row)] = row[arr.index(row)], row[place]
print("\n")
for i in arr:
    print(i, end='\n')
