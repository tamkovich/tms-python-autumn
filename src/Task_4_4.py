x = int(input()) + 1
r = range(1, x)
s = 0
for i in r:
    x = i + 1
    print(x, end=' ')

while x > 1:
    x -= 1
    s = len(r) + 1 - x
    s += 1
    print(s, end=' ')
