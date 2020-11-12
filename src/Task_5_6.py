"""Задан целочисленный массив. Определить количество участков массива,
на котором элементы монотонно возрастают (каждое следующее число
больше предыдущего)."""

import random
n = int(input("Input number of elements in list: "))
arr = random.sample(range(100), n)
print("Исходный массив:", arr)
counter = 0
i = 1
while i < len(arr) - 1:
    if arr[i] > arr[i-1] and arr[i+1] < arr[i]:
        counter += 1
    i += 1
print(counter)
