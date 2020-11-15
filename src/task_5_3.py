for i in range(200, 301):
    dividers_i = 0
    for d in range(1, i // 2 + 1):
        if i % d == 0:
            dividers_i += d
    if 200 <= dividers_i <= 300:
        j = dividers_i
        dividers_j = 0
        for d in range(1, j // 2 + 1):
            if j % d == 0:
                dividers_j += d
        if dividers_j == i:
            print(i, j)

