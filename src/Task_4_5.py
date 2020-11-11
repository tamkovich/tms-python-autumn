p = int(input())
s = 0
b = 1
x = range(1, p+1)
for i in x:
    s, b = b, s + b
    print(s,  end=' ')

while p > 0:
    s, b = b, s + b
    p -= 1
    print(s, end=' ')
