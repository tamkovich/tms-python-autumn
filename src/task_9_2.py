"""Создать lambda функцию, которая принимает на вход неопределенное
количество именных аргументов и выводит словарь
с ключами удвоенной длины. {‘abc’: 5} -> {‘abcabc’: 5}"""
res = (lambda **kwargs: {2 * i: value for i, value in kwargs.items()})(
    aq=1, bw=6, ce=7, dds=3
)
print(res)
