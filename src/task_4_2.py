"""Дан список целых чисел. Подсчитать сколько четных чисел в списке"""
li = list(range(1, 11))
print(li)
num = 0
for i in li:
    if i % 2 == 0:
        num += 1
print(num)
number = 0
while li:
    if li.pop(0) % 2 == 0:
        number += 1
print(number)
