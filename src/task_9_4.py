# Создать универсальный декоратор, который меняет порядок аргументов в
# функции на противоположный


def my_decorator(func):
    def wrapper(arg):
        new_arg = [a for a in arg[::-1]]
        return func(new_arg)

    return wrapper


@my_decorator
def real_func(x):
    print(x)


real_func([1, 2, 3, 7, 8, 10, 89, 66])
