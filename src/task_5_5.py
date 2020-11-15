x = list(range(1, 20))
x1 = list()
lx = len(x)
print(x)
for i in range(lx):
    if x[i] < max(x) and x[i] % 2 == 0:
        x1.append(max(x))
    else:
        x1.append(x[i])
print(x1)
