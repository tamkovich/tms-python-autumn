"""Дан список целых чисел. Создать новый список, каждый элемент которого равен исходному элементу умноженному на -2"""
li = [1, 3, 5, 4, 7, 8]
new_li = list()
for i in li:
   new_li.append(i * (-2))
print(new_li)
new_li2 = list()
while li:
   new_li2.append(li.pop(0) * (-2))
print(new_li2)
