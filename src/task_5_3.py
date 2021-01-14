"""Два натуральных числа называют дружественными, если каждое из них
равно сумме всех делителей другого, кроме самого этого числа. Найти все
пары дружественных чисел, лежащих в диапазоне от 200 до 300."""


x = list(range(200, 301))
a = list()
counter = 0
print(x)
for elem in x:
    for y in range(1, elem // 2 + 1):
        if elem % y == 0 and elem != y:
            counter += y
    a.append(counter)
    counter = 0
print(a)

for i in range(1, len(x)):
    for j in range(1, len(a)):
        if x[i] == a[j] and a[i] == x[j]:
            print("Дружественные числа:", x[i])
