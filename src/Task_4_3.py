dict_1 = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
keys = list(dict_1.keys())
values = list(dict_1.values())
i = 0
new_dict = {}

for key, value in dict_1.items():
    print(key, len(key), value)

while i <= len(keys) - 1:
    i += 1
    x = str(keys[i-1]) + ' ' + str(len(keys[i-1])) + ' ' + values[i-1]
    print(x)
