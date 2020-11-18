# for
x = [1, 2, 3, 4, 5, 6]
y = []
for i in x:
        y.insert(len(y)-1, i)
print(y)

# while
x = [1, 2, 3, 4, 5, 6]
y = []
i = 1
while i < len(x) + 1:
    y.insert(len(y) - 1, i)
    i += 1
print(y)