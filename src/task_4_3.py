# while
d = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
x = list(d.keys())
y = list(d.values())
z={}
i = 0
while i <= len(x)-1:
    z[x[i] + str(len(x[i]))] = y[i]
    i+=1
print(z)

# for
d = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
x = list(d.keys())
y = list(d.values())
d2 = {x[i] + str(len(x[i])): y[i]
for i in range(len(list(x)))}
print(d2)

