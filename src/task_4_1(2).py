
'''Дан список целых чисел.
Создать новый список, каждый элемент которого равен исходному элементу
умноженному на -2'''


a = [1, 2, 3, 4]
s = []
for item in a:
    s.append(item * -2)
print(s)
