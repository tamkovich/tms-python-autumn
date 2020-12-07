N = input('Введите число:', )
if N.isdigit() == True
    N = int(N)
    S = 0
    for i in range(1, N + 1):
        S += 1 / i
        print(S)
