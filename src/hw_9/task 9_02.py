"""Создать lambda функцию, которая принимает на вход неопределенное
количество именных аргументов и выводит словарь с ключами удвоенной
длины. {‘abc’: 5} -> {‘abcabc’: 5}"""

my_function = lambda **kwargs: {key * 2: value for key, value in kwargs.items()}
print(my_function(abc = 5, bla = 3, python = 4, TMS = 7))
