"""В массиве целых чисел с количеством элементов 19 определить максимальное
число и заменить им все четные по значению элементы."""

import random
arr = random.sample(range(100), 19)
print("Исходный массив:", arr)
max_arr = max(arr)
print("Максимальный элемент: ", max_arr)
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        arr[i] = max_arr
print("Новый массив:", arr)
