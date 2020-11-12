"""Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’: ‘value’})."""
diction = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
dict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
for i in diction.keys():
    dict[i + str(len(i))] = dict.pop(i)
print(diction)
print(dict)
dict1 = {}
valueList = list(diction.values())
keysList = list(diction.keys())
i = 0
while i < len(valueList):
    dict1[keysList[i] + str(len(keysList[i]))] = valueList[i]
    i += 1
print(dict1)
