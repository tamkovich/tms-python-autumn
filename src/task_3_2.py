n=float(input("Введите количество людей:"))
if n > 50:
    print("ресторан")
elif n >= 20 and n <=50:
    print("кафе")
elif n < 20:
    print("дом")