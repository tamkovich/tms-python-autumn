# Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’:
# ‘value’}). Чтобы получить список ключей - использовать метод .keys()
# (подсказка: создается новый ключ с цифрой в конце, старый удаляется)
slounik = {
    'test': 'test value',
    'europe': 'eur',
    'dolor': 'usd',
    'rubel': 'rur'
}
drugi = {}
for key in slounik:
    new_key = key + str(len(key))
    drugi[new_key] = slounik[key]
print(slounik)
print('------')
print(drugi)

slounik = {
    'test': 'test value',
    'europe': 'eur',
    'dolor': 'usd',
    'rubel': 'rur'
}
drugoi = {}
while len(drugoi.keys()) != 4:
    slounik.keys() = len(slounik.keys)

#     y = len(x)
# print(x, y)
    # new_key = key + str(len(key))
    # drugoi[new_key] = slounik[key]
# print(drugoi)
