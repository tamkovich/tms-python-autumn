"""Два натуральных числа называют дружественными, если каждое из них равно
 сумме всех делителей другого,кроме самого этого числа. Найти все пары
 дружественных чисел, лежащих в диапазоне от 200 до 300."""
x = list(range(200, 301))
a = list()
counter = 1
print(x)
for elem in x:
    for y in range(2, elem // 2 + 1):
        if elem % y == 0:
            counter += y
    a.append(counter)
    counter = 1
print(a)

len_numbers = len(x)
range_ = range(1, len_numbers)
for i in range_:
    for j in range_:
        if x[i] == a[j] and a[i] == x[j]:
            print("дружественное число ", x[i])
