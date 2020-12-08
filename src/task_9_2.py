# Создать lambda функцию, которая принимает на вход неопределенное
# количество именных аргументов и выводит словарь с ключами удвоенной
# длины. {‘abc’: 5} -> {‘abcabc’: 5}

x = (lambda **kwargs: {key * 2: value for key, value in kwargs.items()})\
     (abc=5, trd=7)
print(x)
