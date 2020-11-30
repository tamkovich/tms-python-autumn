"""Создать декоратор для функции, которая принимает список чисел.
Декоратор должен производить предварительную проверку данных -
удалять все четные элементы из списка."""

def dekorator(func):
    def fake_func(*args):
        s = func(*args)
        res = []
        for i in range(len(s)):
            if s[i] % 2 != 0:
                res.append(s[i])
        return res

    return fake_func


@dekorator
def spisok_chisel():
    spisok = [1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 8, 8, 8, 8, 13]
    return spisok


a = spisok_chisel()
print(a)
