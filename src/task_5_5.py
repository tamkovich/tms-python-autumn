# В массиве целых чисел с количеством элементов 19 определить максимальное
# число и заменить им все четные по значению элементы.

from random import randint

N = 19
i = 0

_list = [randint(-100, 100) for _i in range(N)]
print(_list)
mx = max(_list)
print('maximum = ', mx)

while i < N:
    if _list[i] % 2 == 0:
        _list[i] = mx
        i += 1
    else:
        i += 1
print(_list)
