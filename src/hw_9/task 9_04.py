"""Создать универсальный декоратор, который меняет порядок аргументов в
функции на противоположный."""
def universal_decorator(function):
    def reverse(*args: list) -> function or str:
        """
        Функция принимает список из чисел и, если он состоит только из чисел возвращает reverse list
        :param args: list with numbers
        :return: reverse list
        """
        try:
            return function(*args[::-1])
        except TypeError:
            return "Bad input, try again!"
    return reverse


@universal_decorator
def my_function(*args: list):
    """
    Функция печатает reverse list
    :param args: reverse list with numbers
    """
    return (args)

print(my_function("a","b","c","d","e","f"))
print(my_function(1, 2, 3, 4, 5))
