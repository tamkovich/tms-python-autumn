n = int(input("Введите количество гостей"))
if n>50:
    print("Ресторан")
elif n>20 and n<50:
    print("Кафе")
else:
    print("Дома")