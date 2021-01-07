"""Дан список строк. Отформатировать все строки в формате
‘{i} - {string}’, где i это порядковый номер строки в списке.
 Использовать генератор списков."""
new_str = ["igor", "zeka", "artem", "nikita"]
first_str = [f"{index+1}-{value}" for index, value in enumerate(new_str)]
print(first_str)
