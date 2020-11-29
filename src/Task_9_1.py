"""Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, где i
это порядковый номер строки в списке. Использовать генератор списков."""
new_str = ["Dima", "Mihail", "Valera", "Kostia"]
upd_str = [f'{key} - {value}' for key, value in enumerate(new_str)]
print(upd_str)

# Для тренировки выполнение через lambda функцию
upd_str2 = lambda arr: [f'{new_str.index(name)} - {name}' for name in arr]
print(upd_str2(new_str))
