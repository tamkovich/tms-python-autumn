# 7) Дана целочисленная квадратная матрица. Найти в каждой строке наи-
# больший элемент и поменять его местами с элементом главной диагонали.

import random

counter = 0
print("vvedite kolichestvo strok:")
m = int(input())
print("Vvedite kolichestvo stolbcov")
n = int(input())
stroka = [[random.randint(0, 1000) for z in range(n)] for c in range(m)]
for z in stroka:
    print(z)
for b in stroka:
    indeks = b.index(max(b))
    if indeks != counter:
        b[indeks], b[counter] = b[counter], b[indeks]
    counter += 1

    if counter > m or counter == n:
        break
print("")
for i in stroka:
    print(i)
    # Данная программа, кстати, может считать не только квадратные матрицы
