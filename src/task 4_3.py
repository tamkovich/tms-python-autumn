d = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
a = list(d.keys())
list_of_values = list(d.values())
list_of_key = []

for key in a:
    key = key + str(len(key))
    list_of_key.append(key)
result = dict(zip(list_of_key, list_of_values))
print("result from for:\n ", result)

i = 0
while len(a) > i :
    key = key + str(len(key))
    list_of_key.append(key)
    i += 1
print("result from while: \n ", result )
