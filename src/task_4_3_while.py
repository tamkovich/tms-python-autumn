#Дан словарь:
# {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
#Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’:
#‘value’}). Чтобы получить список ключей - использовать метод .keys()

d = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}

number_key = 0
list_keys = list(d.keys())
len_keys = len(d.keys())
list_new_keys = []

while number_key < len_keys:
    new_key = list_keys[number_key] + str(len(list(list_keys[number_key])))
    list_new_keys.append(new_key)
    d[list_new_keys[number_key]] = d.pop(list_keys[number_key])
    number_key += 1
print(d)



