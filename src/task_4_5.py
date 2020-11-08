# for
x = 15
y = [1, 1]
for i in range(x - 2):
    y.append(y[i] + y[i + 1])
print(y)

# While
x = 15
y = [1, 1]
i = 0
while i <=x - 3:
    y.append(y[i] + y[i + 1])
    i += 1
print(y)
