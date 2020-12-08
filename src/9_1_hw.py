# Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, где i
# это порядковый номер строки в списке. Использовать генератор списков.

spisok_strok = ['Stroka_1', 'Stroka_2', 'Stroka_3', 'Stroka_4']
spisok_str = {f"{index + 1} - {value}" for index, value in enumerate(spisok_strok)}
print(spisok_str)