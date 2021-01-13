"""Введите число. Если это число делиться на 1000 без остатка, то выведите на
экран "millennium"""


print("Vvedite chiclo")
a = input()
if int(a) % 1000 == 0:
    print("millennium")
else:
    print("not millennium")
