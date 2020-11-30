# Создать lambda функцию, которая принимает на вход неопределенное
# количество именных аргументов и выводит словарь с ключами удвоенной
# длины.
dict1 = {"123": "Dog", "456": "Parrot", "789": "Cat", "qwe": "Croco"}
dictfunc = dict(map(lambda key: (key * 2, dict1[key]), dict1))
print(dict(dictfunc))
