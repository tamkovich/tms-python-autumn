import random
N = int(input("vvedite razmer kvadratnoi matrici:"))
matrix = []
for i in range(N):
    row = []
    for j in range(N):
        row.append(random.randint(1, 9))
    matrix.append(row)
print(matrix)
for i in range(N):
    j=0
    for e, value in enumerate(matrix[i]):
        if matrix[i][j]<value:
            j=e
    m=matrix[i][j]
    matrix[i][j]=matrix[i][i]
    matrix[i][i]=m
print(matrix)
