""" Создать декоратор для функции, которая принимает список чисел.
Декоратор должен производить предварительную проверку данных -
удалять все четные элементы из списка."""

from functools import wraps


def check_even(func):
    """Функция проверяет список на четные числа и удаляет их из списка"""
    @wraps(func)
    def evens(*args: int) -> list:
        arr = []
        for i in args:
            if i % 2 != 0:
                arr.append(i)
        return arr
    return evens


@check_even
def numbers(*args: int) -> list:
    """Принимает список чисел"""
    return list(args)


print(numbers(1, 2, 3, 4))
