"""Создать декоратор для функции, которая принимает список чисел.
Декоратор должен производить предварительную проверку данных -
удалять все четные элементы из списка."""
from functools import wraps


def new_func(real_func):
    """A function that accepts another function"""
    @wraps(real_func)
    def fake_func(*args: int) -> list:
        """Decorator for delete odd elements"""
        li = []
        for i in args:
            if i % 2 != 0:
                li.append(i)
        return li

    return fake_func


@new_func
def func(*args: int) -> tuple:
    """function returning arguments"""
    return args


print(func(1, 4, 7, 4, 6, 3))
