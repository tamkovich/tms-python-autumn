"""Создать lambda функцию, которая принимает на вход неопределенное
количество именных аргументов и выводит словарь с ключами удвоенной
длины. {‘abc’: 5} -> {‘abcabc’: 5}"""

new_dict = {"123": "Dima", "abs": "Leha", "a23": "Mihail"}
upd_dict = dict(map(lambda key: (key + key, new_dict[key]), new_dict))
print(upd_dict)
