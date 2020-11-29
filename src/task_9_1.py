# Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, где i
# это порядковый номер строки в списке. Использовать генератор списков.


a = [i for i in 'abcdef']
for j in a:
    print(a.index(j), "-", j)

print("----------")

b = [_i for _i in 'abcdef']
for _j in enumerate(b):
    print(_j)
