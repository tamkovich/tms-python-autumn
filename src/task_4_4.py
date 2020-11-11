a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

for i in a:
    a.append(a[0])
    a.reverse()
    a.pop(-1)
    a.reverse()
    print(a)
