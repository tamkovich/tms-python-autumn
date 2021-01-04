"""В массиве целых чисел с количеством элементов 19 определить максимальное
# число и заменить им все четные по значению элементы. [02-4.1-BL19]"""

import random

a = []
n = int(input())
for i in range(0, n):
    x = random.randint(0, 10000)
    a.append(x)
for g in range(0, len(a) - 1):
    if a[g] % 2 == 0:
        a[g] = max(a)
print(a)
print(max(a))
