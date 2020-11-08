a = [1, 2, 3, 4]
s = []
while True:
    if len(a) == 1:
        s.append(a[0])
        break
    else:
        x = a.pop(1)
        s.append(x)
        print(s)
print(s)
