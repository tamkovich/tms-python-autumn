m = input()
n = input()
if m.isdigit() and n.isdigit():
    m = int(m)
    n = int(n)
    x = list(range(m, n+1))
    lx = len(x)
    matrix = []
    for number in range(0, lx):
        y = []
        for delitel in range(2, n):
            if x[number] % delitel == 0 and x[number] != delitel:
                y.append(delitel)
        matrix.append(y)
    print(matrix)
