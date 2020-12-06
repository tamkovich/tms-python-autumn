"""В массиве целых чисел с количеством элементов 19
определить максимальное число и заменить им все четные по значению элементы."""
import random

massiv = []
for i in range(19):
    a = random.randint(1, 100)
    massiv.append(a)
print(massiv)
max_value = max(massiv)
print(f"max_value  {max_value}")
for i in range(len(massiv)):
    if massiv[i] % 2 == 0:
        massiv[i] = max_value
print(massiv)
