'''Дан список. Создать новый список, сдвинутый на 1 элемент влево
Пример: 1 2 3 4 5 -> 2 3 4 5 1'''


a = [1, 2, 3, 4]
s = []
while True:
    if len(a) == 1:
        s.append(a[0])
        break
    else:
        x = a.pop(1)
        s.append(x)
        print(s)
print(s)
