"""Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, где i
это порядковый номер строки в списке. Использовать генератор списков."""

words = ["Hello", "World", "Belarus"]
index_words=[f'{i} - {e}' for i, e in enumerate(words)]
print(index_words)