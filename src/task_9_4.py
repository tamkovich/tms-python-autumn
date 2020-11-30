"""Создать универсальный декоратор, который меняет порядок аргументов в
функции на противоположный."""

def dekorator(real_func):
    def fake_func(*args):
        a = args[::-1]
        return a
    return fake_func


@dekorator
def func(*args):
    return args

print(func(1, 4, 7, 4, 6, 3))
print(func("petr", "alex", "pitonisti"))
