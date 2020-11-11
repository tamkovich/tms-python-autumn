# Выполнение с циклом for
n = int(input("Введите длинну списка: "))
spisok1 = list(range(1, n))
spisok2 = [i * 2 for i in spisok1]
print(spisok2)

# Выполнение с циклом while
n = int(input("Введите длинну списка: "))
spisok1 = list(range(1, n))
spisok2 = list()
i = 1
while i <= len(spisok1):
    spisok2.append(i * 2)
    i += 1
print(spisok2)
