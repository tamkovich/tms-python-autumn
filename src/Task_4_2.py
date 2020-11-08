z = int(input())
x = list(range(1, z+1))
s = 0
c = 0
y = len(x)

for i in x:
    if i % 2 == 0:
        s += 1
print(s)

while y > 0:
    y -= 1
    if y % 2 == 0:
        s += 1
print(s)