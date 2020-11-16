m = int(input("Введите нижнию границу промежутка: "))
n = int(input("Введите верхнию границу промежутка: "))
x = []
for i in range(m, n+1):
    for j in range(2, i//2 + 1):
        if i % j == 0:
            x.append(j)
    print(f'{i}: {" ".join(map(str, x))}')
    x.clear()
