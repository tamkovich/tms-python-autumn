"""Дана целочисленная квадратная матрица. Найти в каждой строке
наибольший элемент и поменять его местами с элементом главной диагонали."""
import random

matrix = []
n = int(input())
for number_rows in range(n):
    box1 = []
    for number_cols in range(n):
        box1.append(random.randint(1, 9))
    max_value = max(box1)
    index = box1.index(max_value)
    matrix.append(box1)
    print(box1)
    print(f"max value in {number_rows+1} box : {max_value}")
    print(f"value diagonal {matrix[number_rows][number_rows]}")
    matrix[number_rows][index] = int(matrix[number_rows][number_rows])
    matrix[number_rows][number_rows] = max_value
print(matrix)
