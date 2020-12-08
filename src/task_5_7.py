matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for i in range(0, 3):
    for j in range(0, 3):
        if matrix[i][j] >= max(matrix[i]):
            if i == 0:
                matrix[0].insert(0, max(matrix[i]))
                matrix[0].pop(-1)
            elif i == 1:
                matrix[1].insert(1, max(matrix[i]))
                matrix[1].pop(-1)
            elif i == 2:
                matrix[2].insert(2, max(matrix[i]))
                matrix[2].pop(-1)
print(matrix)
