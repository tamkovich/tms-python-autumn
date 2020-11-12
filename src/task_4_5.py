"""Составить список чисел Фибоначчи содержащий 15 элементов."""
b = a = 1
li = [a, b]
c = 0
for i in range(1, 14):
    c = a + b
    li.append(c)
    a = b
    b = c
print(li)
b1 = a1 = 1
li1 = [a1,b1]
c1 = i = 0
while i < 13:
    c1 = a1 + b1
    li1.append(c1)
    a1 = b1
    b1 = c1
    i += 1
print(li1)
