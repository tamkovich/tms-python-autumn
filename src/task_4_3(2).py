a = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
b = list(a.keys())
f = a.values()
s = []
for i in range(4):
    x = b.pop(0)
    x += str(len(x))
    s.append(x)
g = dict(zip(s, f))
print(g)
