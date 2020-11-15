x = [1, 2, 3, 2, 1, 3, 5, 7, 3, 1, 6, 7]
lx = len(x)
matrix = []
y = []
for i in range(0, 1):
    for j in range(0, lx):
        if j == lx - 1:
            matrix.append(y)
        elif x[j] < x[j + 1] or x[j] > x[j - 1]:
            y.append(x[j])
        else:
            matrix.append(y)
            y = []
print(len(matrix))
