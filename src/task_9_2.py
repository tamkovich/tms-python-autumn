# Создать lambda функцию, которая принимает на вход неопределенное
# количество именных аргументов и выводит словарь с ключами удвоенной
# длины. {‘abc’: 5} -> {‘abcabc’: 5}

dict_1 = {"jhjgjf": 1, "uvghugh": 2, "yfegfeg": 3, "yfgeugf": 4, "jfbejfb": 5}
print(dict_1)
func = map(lambda key: (key * 2, dict_1[key]), dict_1)
print(dict(func))
