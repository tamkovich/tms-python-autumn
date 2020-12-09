# Создать универсальный декоратор, который меняет порядок аргументов в
# функции на противоположный.

def decorator(func):
    def wrapper(arg):
        """Функция меняет порядок аргументов на противоположный."""
        new_arg = [a for a in arg[::-1]]
        return func(new_arg)

    return wrapper


@decorator
def function(x):
    return x


print(function([1, 2, 3, 4, 5, 6, 7, 8, 9]))
