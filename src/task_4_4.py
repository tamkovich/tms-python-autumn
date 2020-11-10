#Дан список. Создать новый список, сдвинутый на 1 элемент влево
#Пример: 1 2 3 4 5 -> 2 3 4 5 1

a = int(input('start of list: '))
b = int(input('end of list: '))


first_list = list(range(a, b + 1)) # получаем список
second_list = first_list[1:] # удаляем первую цифру
third_list = first_list[:1] # удвляем всё, кроме первой цифры
finish = second_list + third_list
print(finish)
