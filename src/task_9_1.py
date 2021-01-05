"""Дан список строк. Отформатировать все строки в формате
‘{i} - {string}’, где i
это порядковый номер строки в списке. Использовать
генератор списков."""

list_1 = ["adshdhashd", "dfhkhfk", "kdjfbdkjf", "kjkjdvlasd", "agfugffhf"]
list_2 = [f"{key} - {value}" for key, value in enumerate(list_1)]
print(list_2)
