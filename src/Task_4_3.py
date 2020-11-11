""" Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’:
‘value’}). Чтобы получить список ключей - использовать метод .keys()"""

# С использованием цикла for
_dict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
keys = list(_dict.keys())
values = list(_dict.values())
new_dict = {keys[i] + str(len(keys[i])): values[i] for i in range(len(list(keys)))}
print(new_dict)
# С использованием цикла while
_dict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
keys1 = list(_dict.keys())
values1 = list(_dict.values())
new_dict2 = {}
i = 0
while i <= len(keys1)-1:
    new_dict2[f"{keys1[i]}{len(keys1[i])}"] = values1[i]
    i += 1
print(new_dict2)
