# while
a = [6,4,5,8,9,11]
s = 0
i = 0
while a:
    x = int(a.pop())
    if x % 2 == 0:
        s += 1
    i += 1
print(s)

# for
a = [6,4,5,8,9,11]
s = 0
i = 0
for i in a:
    if i % 2 ==0:
        s += 1
print(s)
