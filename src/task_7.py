"""Написать 12 функций по переводу:
Дюймы в сантиметры
Сантиметры в дюймы
Мили в километры
Километры в мили
Фунты в килограммы
Килограммы в фунты
Унции в граммы
Граммы в унции
Галлон в литры
Литры в галлоны
Пинты в литры
Литры в пинты
Примечание: функция принимает на вход число и
возвращает конвертированное число"""


def perevod(y, x):
    dict = {
        1: duim_sm,
        2: sm_duim,
        3: mile_km,
        4: km_mile,
        5: funt_kg,
        6: kg_funt,
        7: unc_gr,
        8: gr_unc,
        9: gl_litr,
        10: litr_gl,
        11: litr_pint,
        12: pint_litr,
    }
    while True:
        print("Введите номер операции:")
        y = input()
        if y.isdigit():
            y = int(y)
        if y == 0:
            print("Конец операции")
            break
        else:
            print("Введите число для перевода:")
            x = float(input())
            print(dict[y](x))


def duim_sm(x: float) -> float:
    print("Дюймы в сантиметры")
    return x * 2.54


def sm_duim(x: float) -> float:
    print("Сантиметры в дюймы")
    return x / 2.54


def mile_km(x: float) -> float:
    print("Мили в километры")
    return x * 1.609


def km_mile(x: float) -> float:
    print("Километры в мили")
    return x / 1.609


def funt_kg(x: float) -> float:
    print("Фунты в килограммы")
    return x / 2.2046


def kg_funt(x: float) -> float:
    print("Килограммы в фунты")
    return x * 2.2046


def unc_gr(x: float) -> float:
    print("Унции в граммы")
    return x * 28.35


def gr_unc(x: float) -> float:
    print("Граммы в унции")
    return x / 28.35


def gl_litr(x: float) -> float:
    print("Галлон в литры")
    return x * 3.785


def litr_gl(x: float) -> float:
    print("Литры в галлоны")
    return x / 3.785


def litr_pint(x: float) -> float:
    print("Пинты в литры")
    return x * 2


def pint_litr(x: float) -> float:
    print("Литры в пинты")
    return x / 2


perevod(1, 1)
