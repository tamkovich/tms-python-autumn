a = [1, 2, 3, 4]
s = []
for i in range(4):
    if i != 0:
        s.append(a[i])
s.append(a[0])
print(s)
