# Дано число. Найти сумму и произведение его цифр.

a = input('Введите число: ')
_len_a = len(a)
_list_a = list(a)
s = 0
m = 1

if _len_a == 1:
    print('число состоит из одной цифры', a)

if _len_a > 1:
    for i in _list_a:
        s += int(i)
        m *= int(i)
    print('summa = ', s)
    print('multiplication = ', m)
