""" Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, где i
это порядковый номер строки в списке. Использовать генератор списков. """

my_list = ["stroka1", "stroka2", "stroka3", "stroka4"]

z = [f"{x} - {z}" for x, z in enumerate(my_list, start=1)]

print(z)
