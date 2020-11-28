"""Создать универсальный декоратор, который меняет порядок
 аргументов в функции на противоположный."""
from functools import wraps


def new_func(real_func):
    """A function that accepts another function"""
    @wraps(real_func)
    def fake_func(*args: any) -> tuple:
        """Decorator to reverse"""
        li = args[::-1]
        return li
    return fake_func


@new_func
def func(*args: any) -> tuple:
    """function returning arguments"""
    return args


print(func(1, 4, 7, 4, 6, 3))
print(func("igor", "artem", "tolia"))
