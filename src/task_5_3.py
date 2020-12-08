summa = 1
list_summa = list()
list_element = list(range(200, 301))
for i in list_element:
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            summa += j
    list_summa.append(summa)
    summa = 1
print(list_element)
print(list_summa)

for element in range(1, len(list_element)):
    for number in range(1, len(list_summa)):
        if list_element[element] == list_summa[number] and\
                list_element[number] == list_summa[element]:
            print('Дружественное число:', list_element[element])
