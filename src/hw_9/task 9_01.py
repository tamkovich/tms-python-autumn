"""Дан список строк. Отформатировать все строки в формате {i}-{string}, где
i это порядковый номер строки в списке. Использовать генератор списков."""

list_of_string = [
    "Ihar",
    "Zeka",
    "wolf",
    "cat",
    "dog"
]

print([f"{index} : {element}" for index, element in enumerate(list_of_string)])
