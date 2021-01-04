kolvo = 15
a = int(input("print first number of your fibonacci series"))
b = a
s = 0
n = 0
while n < kolvo:
    s = a + b
    a = b
    b = s
    n += 1
    print(s)


kolvo = 15
a = int(input("print first number of your fibonacci series"))
b = a
s = 0
for i in range(kolvo):
    s = a + b
    a = b
    b = s
    print(s)
