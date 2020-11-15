N = int(input("vvedite N: "))
M = int(input("vvedite M: "))
delitel_i = []
deliteli = []
for i in range(N, M + 1):

    for d in range(2, i // 2 + 1):
        if i % d == 0:
            delitel_i.append(d)

    if not delitel_i:
        delitel_i.append("Нет делителей")
    deliteli.append(delitel_i)
    delitel_i = []

for i in range(len(deliteli)):
    print(f"Делители числа {N + i}: {deliteli[i]}")
