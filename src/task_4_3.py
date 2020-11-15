#Цикл For
dict1={'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
keys=list(dict1.keys())
values=list(dict1.values())
new_dict=dict()
for i in range(len(keys)):
    new_dict[keys[i] + str(len(keys[i]))]=values[i]
print (new_dict)

#Цикл While
dict1={'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
keys=list(dict1.keys())
values=list(dict1.values())
new_dict=dict()
i=0
while i <= len(keys)-1:
    new_dict[keys[i] + str(len(keys[i]))]=values[i]
    i+=1
print (new_dict)
