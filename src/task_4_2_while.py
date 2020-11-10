#Дан список целых чисел. Подсчитать сколько четных чисел в списке

_list = list(range(0, 11))
i = 0
count = 0
_len = len(_list)

while i < _len:
    if _list[i] % 2 == 0:
        count += 1
        i += 1
    else:
        i += 1
print(count)