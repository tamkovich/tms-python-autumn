'''Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’:
‘value’}). Чтобы получить список ключей - использовать метод .keys()'''


a = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
b = list(a.keys())
f = a.values()
s = []
while b:
    x = b.pop(0)
    x += str(len(x))
    s.append(x)
g = dict(zip(s, f))
print(g)
