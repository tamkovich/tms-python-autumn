# Создать декоратор для функции, которая принимает список чисел.
# Декоратор должен производить предварительную проверку данных -
# удалять все четные элементы из списка.


def my_decorator(func):
    def wrapper(arg):
        new_arg = [a for a in arg if a % 2]
        return func(new_arg)

    return wrapper


@my_decorator
def real_func(x):
    print(x)


real_func([1, 2, 3, 7, 8, 10, 89, 66])
