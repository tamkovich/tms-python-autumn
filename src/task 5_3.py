x = list(range(200, 301))
a = list()
counter = 1
for elem in x:
    for y in range(counter+1, (elem//2+2)):
        if elem % y == 0 and elem != y:
            counter += y
    a.append(counter)
    counter = 0
print(a)
n = len(x)
for i in range(1, n):
    for j in range(1, n):
        if x[i] == a[j] and a[i] == x[j]:
            print(x[i])

