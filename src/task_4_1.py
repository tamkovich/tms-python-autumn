s = 0
x = int(input())
r = list(range(1, x))

for i in r:
    s = i * -2
    print(s, end=' ')

while x > 1:
    x -= 1
    s = (len(r) + 2 - x) * -2
    s += 2
    print(s, end=' ')
