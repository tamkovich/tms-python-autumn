# С использованием цикла for
dict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
keys = list(dict.keys())
values = list(dict.values())
new_dict = {keys[i]+str(len(keys[i])): values[i] for i in range(len(list(keys)))}
print(new_dict)
# С использованием цикла while
dict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
keys1 = list(dict.keys())
values1 = list(dict.values())
new_dict2 = {}
i = 0
while i <= len(keys1)-1:
    new_dict2[keys1[i] + str(len(keys1[i]))] = values1[i]
    i += 1
print(new_dict2)
