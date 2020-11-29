# Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, где i
# это порядковый номер строки в списке. Использовать генератор списков.

list_str = ['String', 'List', 'Tuple']
x = [f'{i}-{list_str[i]}' for i in range(len(list_str))]
print(x)
