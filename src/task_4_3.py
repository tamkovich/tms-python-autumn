dict = {"test": "test_value", "europe": "eur", "dollar": "usd", "ruble": "rub"}
number = 0
newkey = 0
mydict = dict.copy()
for key_old, value in mydict.items():
    number = len(key_old)
    newkey = str(key_old) + str(number)
    dict[newkey] = dict.pop(key_old)
print(dict)
