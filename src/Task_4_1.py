"""Дан список целых чисел.
Создать новый список, каждый элемент которого равен исходному элементу
умноженному на -2"""

# Выполнение с циклом for
try:
    n = int(input("Введите длинну списка: "))
except ValueError:
    print("Что-то ты не то ввел дружище!")
else:
    spisok1 = list(range(1, n))
    spisok2 = [i * -2 for i in spisok1]
    print(spisok2)

# Выполнение с циклом while
try:
    n = int(input("Введите длинну списка: "))
except ValueError:
    print("Что-то ты не то ввел дружище!")
else:
    spisok1 = list(range(1, n))
    spisok2 = list()
    i = 1
    while i <= len(spisok1):
        spisok2.append(i * 2)
        i += 1
    print(spisok2)
