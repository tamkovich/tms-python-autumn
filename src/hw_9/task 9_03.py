"""Создать декоратор для функции, которая принимает список чисел.
Декоратор должен производить предварительную проверку данных -
удалять все четные элементы из списка."""
import random

def decorator_delete(function):
    def delete_even_elements(*args: list) -> list:
        """
        Функция удаляет все чётные элементы
        :param args: list with numbers
        :return: new list в котором удалены чётные элементы
        """
        return function([i for i in args[0] if i % 2 != 0])
    return delete_even_elements

@decorator_delete
def function_for_decorator(elements: list) -> list or str:
    """
    Функция проверяет тип данных
    :param numbers: list of numbers
    :return: list with uneven numbers or message
    """
    try:
        return elements
    except TypeError:
        return "Bad input, try again!"

list_of_elements = [random.randint(0,1000) for i in range(10)]
print(f"input_data:{list_of_elements}\n",f"check_data:{function_for_decorator(list_of_elements)}")
