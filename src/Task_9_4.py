"""Создать универсальный декоратор, который меняет порядок аргументов в
функции на противоположный."""

from functools import wraps


def reverse_args(func):
    wraps(func)
    """Возвращает аргументы в обратном порядке"""
    def reverse(*args):
        result = func(*args)
        return result[::-1]
    return reverse


@reverse_args
def spisok(*args):
    """Принимает аргументы"""
    return args


print(spisok(1, 'a', 2, 'b'))
