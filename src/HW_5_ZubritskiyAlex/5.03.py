#Два натуральных числа называют дружественными, если каждое из них
#равно сумме всех делителей другого, кроме самого этого числа. Найти все
#пары дружественных чисел, лежащих в диапазоне от 200 до 300.

x = list(range(200, 301))
a = list()
counter = 1 # учитыв 1 не учит число

for elem in x:
    for y in range(1, elem//2 + 1):
        if elem % y == 0:
            counter += y
    a.append(counter)
    counter = 1

length_numbers = len(x)

for i in range(1, length_numbers):
    for j in range(1, length_numbers):
        if x[i] == a[j] and a[i] == x[j]:
            print(" friendly: ", x[i])
