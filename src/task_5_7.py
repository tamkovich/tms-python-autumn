# Дана целочисленная квадратная матрица. Найти в каждой строке наи-
# больший элемент и поменять его местами с элементом главной диагонали.

# CREATE MATRIX
import random

n = int(input())
matrix = []
for i in range(n):
    box = []
    for i in range(n):
        box.append(random.randint(0, 10))
    matrix.append(box)
print("start matrix:", matrix)

# CREATE LIST OF MAXIMUM
list_maximum = []
for i in matrix:
    mx = max(list(i))
    list_maximum.append(mx)
# print('list of maximum: ', list_maximum)

# CREATE INDEX LIST OF MAXIMUM
y = 0
index_maximum = []
for j in matrix:
    index_maximum.append(j.index(list_maximum[y]))
    y += 1
# print("index of max: ", index_maximum)

# CREATE FINISH MATRIX
index_row = 0
index_col = 0
index_max_list = 0

while index_col < len(matrix[0]):
    diagonale = matrix[index_row][index_col]
    maximale = list_maximum[index_col]
    matrix[index_row][index_col] = maximale
    matrix[index_row][index_maximum[index_max_list]] = diagonale
    index_row += 1
    index_col += 1
    index_max_list += 1
print("finish: ", matrix)
