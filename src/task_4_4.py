"""Дан список. Создать новый список, сдвинутый на 1 элемент влево Пример:12345-> 23451"""
list = [34, 56, 21, 65]
list.append(list.pop(0))
print(list)
list1 = [34, 56, 21, 65]
new_list = []
for i in list1:
        new_list.insert(len(new_list)-1, i)
print(new_list)
new_list2 = []
while list1:
    new_list2.insert(len(new_list2) - 1, list1.pop(0))
print(new_list2)
