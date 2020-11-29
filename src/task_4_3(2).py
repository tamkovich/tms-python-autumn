a = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
b = list(a.keys())
f = a.values()
s = []
for i in range(4):
    x = b.pop(0)
    s.append(f"{x}{len(x)}"
g = dict(zip(s, f))
print(g)
