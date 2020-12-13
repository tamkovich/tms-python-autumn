# Задан целочисленный массив. Определить количество участков массива,
# на котором элементы монотонно возрастают (каждое следующее число
# больше предыдущего).

from random import randint

_list = [randint(0, 10) for i in range(8)]

print(_list)
index = 0
count = 0

while index <= 8:
    if _list[index:index + 1] < _list[index + 1:index + 2]:
        if _list[index:index + 1] >= _list[index + 1:index + 2]:
            index += 1
        index += 1
        count += 1
    index += 1
print(count)
