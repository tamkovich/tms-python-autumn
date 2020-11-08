a = [1, 2, 3, 4]
s = 0
while a:
    x = a.pop(0)
    if x % 2 == 0:
        s += 1
print(s)
