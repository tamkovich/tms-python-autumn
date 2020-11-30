# Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, где i
# это порядковый номер строки в списке. Использовать генератор списков.
list = ["Dog", "Cat", "Parrot", "Crocodile"]
new_list = [f'{key} - {value}' for key, value in enumerate(list, 1)]
print(new_list)
