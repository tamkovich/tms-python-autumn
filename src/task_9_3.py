# Создать декоратор для функции, которая принимает список чисел.
# Декоратор должен производить предварительную проверку данных -
# удалять все четные элементы из списка.
import random

list_1 = [random.randint(0, 1000) for i in range(20)]
print(list_1)


def decorator(func):
    def my_reducing(x):
        result = filter(lambda x: x % 2 != 0, list_1)
        return result

    return my_reducing


@decorator
def reducing(x):
    pass


print(list(reducing(list_1)))
