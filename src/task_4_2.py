"""Дан список целых чисел. Подсчитать сколько
четных чисел в списке"""


s = 0
a = [19, 22, 54, 6, 54, 3, 2, 43, 22, 154]
for i in a:
    if i % 2 == 0:
        s += 1
print(s)

s = 0
a = [19, 22, 54, 6, 54, 3, 2, 43, 22, 154]
while a:
    x = a.pop()
    if x % 2 == 0:
        s += 1
print(s)
