'''Написать 12 функций по переводу:
    1.Дюймы в сантиметры
    2.Сантиметры в дюймы
    3.Мили в километры
    4.Километры в мили
    5.Фунты в килограммы
    6.Килограммы в фунты
    7.Унции в граммы
    8.Граммы в унции
    9.Галлон в литры
    10.Литры в галлоны
    11.Пинты в литры
    12.Литры в пинты
Примечание: функция принимает на вход число и возвращает конвертированное число'''


def inch_centimeter(inch:float) -> float:
    centimeter = inch * 2.54
    return f'В {inch} дюймах {centimeter} сантиметров.'
def centimeter_inch(centimeter:float) -> float:
    inch = centimeter * 0.393701
    return f'В {centimeter} сантиметрах {inch} дюймов.'
def mile_kilometer(mile:float) -> float:
    kilometer = mile * 1.60934
    return f'В {mile} милях {kilometer} километров.'
def kilometer_mile(kilometer:float) -> float:
    mile = kilometer * 0.621371
    return f'В {kilometer} километрах {mile} мили.'
def pound_kilogram(pound:float) -> float:
    kilogram = pound * 0.453592
    return f'В {pound} футах {kilogram} килогамм.'
def kilogram_pound(kilogram:float) -> float:
    pound = kilogram * 2.20462
    return f'В {kilogram} килограммах {pound} футов.'
def ounce_gram(ounce:float) -> float:
    gram = ounce * 28.3495
    return f'В {ounce} унциях {gram} грамм.'
def gram_ounce(gram:float) -> float:
    ounce = gram * 0.035274
    return f'В {gram} граммах {ounce} унций.'
def gallon_liter(gallon:float) -> float:
    liter = gallon * 4.54609
    return f'В {gallon} галлонах {liter} литров.'
def liter_gallon(liter:float) -> float:
    gallon = liter * 0.219969
    return f'В {liter} литрах {gallon} галлонов.'
def pint_liter(pint:float) -> float:
    liter = pint * 0.568261
    return f'В {pint} пинтах {liter} литров.'
def liter_pint(liter:float) -> float:
    pint = liter * 1.75975
    return f'В {liter} литрах {pint} пинт.'

'''. Написать программу, со следующим интерфейсом: пользователю предоставляется на
выбор 12 вариантов перевода(описанных в первой задаче). Пользователь вводит цифру
от одного до двенадцати. После программа запрашивает ввести численное значение.
Затем программа выдает конвертированный результат. Использовать функции из первого
задания. Программа должна быть в бесконечном цикле. Код выхода из программы - “0”.'''

dict_functions = {
        1: inch_centimeter(value),
        2: centimeter_inch(value),
        3: mile_kilometer(value),
        4: kilometer_mile(value),
        5: pound_kilogram(value),
        6: kilogram_pound(value),
        7: ounce_gram(value),
        8: gram_ounce(value),
        9: gallon_liter(value),
        10: liter_gallon(value),
        11: pint_liter(value),
        12: liter_pint(value)
    }
while True:
    print('1.Дюймы в сантиметры\n'
          '2.Сантиметры в дюймы\n'
          '3.Мили в километры\n'
          '4.Километры в мили\n'
          '5.Фунты в килограммы\n'
          '6.Килограммы в фунты\n'
          '7.Унции в граммы\n'
          '8.Граммы в унции\n'
          '9.Галлон в литры\n'
          '10.Литры в галлоны\n'
          '11.Пинты в литры\n'
          '12.Литры в пинты\n'
          'Введите число от 1 до 12:')
    x = input()
    if x.isdigit() == True:
        x = int(x)
    else:
        print('Введен не правильный тип данных')
        continue
    if x == 0:
        break
    print('Введите величину:  ')
    value = float(input())
   
    if x in dict_functions.keys():
        print(dict_functions[x])
