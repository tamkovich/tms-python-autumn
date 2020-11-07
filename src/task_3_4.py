a = input("Введи строку:")
b = len(a)
c = int(b / 2)
if b > (c * 2):
    print(a[c])
    d = a[c]
else:
    print(a[c - 1])
    d = a[c - 1]
if d == (a[0]):
    e = a[1:(b - 1)]
    print(e)