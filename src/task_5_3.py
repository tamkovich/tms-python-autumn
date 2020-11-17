# Два натуральных числа называют дружественными, если каждое из них
# равно сумме всех делителей другого, кроме самого этого числа. Найти все
# пары дружественных чисел, лежащих в диапазоне от 200 до 300.

number = list(range(200, 301))
list_summa = []
for i in number:
    summa = 0
    for j in range(1, int(300 / 2 + 1)):
        ostatok = i % j
        if ostatok == 0:
            summa = summa + j
    list_summa.append(summa)
print("список сумм: ", list_summa)
print("список чисел:", number)
print("====================")

for q in list(range(0, 101)):
    for w in list(range(0, 101)):
        if list_summa[q] == number[w]:
            if list_summa[w] == number[q]:
                print("дружественное число: ", list_summa[q])
