def d_in_cm(number):  # Дюймы в сантиметры
    x = float(number) * 2.54
    print(x)


def cm_in_d(number):  # Сантиметры в дюймы
    x = float(number) / 2.54
    print(x)


def ml_in_km(number):  # Мили в километры
    x = float(number) * 1.60934
    print(x)


def km_in_ml(number):  # Километры в мили
    x = float(number) / 1.60934
    print(x)


def f_in_kg(number):  # Фунты в килограммы
    x = float(number) * 0.453592
    print(x)


def kg_in_f(number):  # Килограммы в фунты
    x = float(number) * 2.20462
    print(x)


def y_in_gr(number):  # Унции в граммы
    x = float(number) * 28.3495
    print(x)


def gr_in_y(number):  # Граммы в унции
    x = float(number) * 0.035274
    print(x)


def gl_in_lt(number):  # Галлон в литры
    x = float(number) / 3.78541
    print(x)


def lt_in_gl(number):  # Литры в галлоны
    x = float(number) / 0.264172
    print(x)


def pn_in_lt(number):  # Пинты в литры
    x = float(number) / 0.473176
    print(x)


def lt_in_pn(number):  # Литры в пинты
    x = float(number) / 2.11338
    print(x)


def list_of():
    lis = [
        "1.Дюймы в сантиметры",
        "2.Сантиметры в дюймы",
        "3.Мили в километры",
        "4.Километры в мили",
        "5.Фунты в килограммы",
        "6.Килограммы в фунты",
        "7.Унции в граммы",
        "8.Граммы в унции",
        "9.Галлон в литры",
        "10.Литры в галлоны",
        "11.Пинты в литры",
        "12.Литры в пинты",
        "0.Стоп",
    ]
    for i in lis:
        print(i)


while True:
    list_of()
    function_select = int(input())
    print(" ")
    if function_select == 0:
        break
    elif function_select == 1:
        d_in_cm(input("1.Дюймы в сантиметры: "))

    elif function_select == 2:
        cm_in_d(input("2.Сантиметры в дюймы: "))

    elif function_select == 3:
        ml_in_km(input("3.Мили в километры: "))

    elif function_select == 4:
        km_in_ml(input("4.Километры в мили:"))

    elif function_select == 5:
        f_in_kg(input("5.Фунты в килограммы: "))

    elif function_select == 6:
        kg_in_f(input("6.Килограммы в фунты: "))

    elif function_select == 7:
        y_in_gr(input("7.Унции в граммы: "))

    elif function_select == 8:
        gr_in_y(input("8.Граммы в унции: "))

    elif function_select == 9:
        gl_in_lt(input("9.Галлон в литры: "))

    elif function_select == 10:
        lt_in_gl(input("10.Литры в галлоны: "))

    elif function_select == 11:
        pn_in_lt(input("11.Пинты в литры: "))

    elif function_select == 12:
        lt_in_pn(input("12.Литры в пинты: "))

    else:
        print("попробую еще раз")
