"""Задан целочисленный массив. Определить количество участков массива,
на котором элементы монотонно возрастают."""
import random

massiv = []
count = 0
n = int(input("enter n "))
for i in range(n):
    massiv.append(random.randint(1, 100))
print(massiv)
num = massiv[0]
for i in range(1, n):
    if massiv[i] > massiv[i - 1]:
        num = massiv[i]
    elif massiv[i - 1] == num:
        count += 1
print(f" UPˆ {count}")
