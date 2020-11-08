a = [1, 1]
s = [1, 1]
while True:
    if len(s) == 15:
        break
    else:
        x = a[0] + a[1]
        a.append(x)
        a.pop(0)
        s.append(x)
print(s)
