"""Создать универсальный декоратор, который меняет порядок аргументов в
функции на противоположный."""


def decorator():
    def func(*args):
        return args[::-1]

    return func


reverse_argument = decorator()

print(reverse_argument("в лесу", "светлячков"))
