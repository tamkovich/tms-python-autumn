#2. Написать программу, со следующим интерфейсом: пользователю предоставляется на
# выбор 12 вариантов перевода(описанных в первой задаче). Пользователь вводит цифру
# от одного до двенадцати. После программа запрашивает ввести численное значение.
# Затем программа выдает конвертированный результат. Использовать функции из первого
# задания. Программа должна быть в бесконечном цикле. Код выхода из программы - “0”.

def djuim_sm(x: float):
    return x * 2.54

def sm_djuim(x: float):
    return x / 2.54

def miles_km(x: float):
    return x * 1.609

def km_miles(x: float):
    return x / 1.609

def funts_kg(x: float):
    return x / 2.2046

def kg_funts(x: float):
    return x * 2.2046

def unc_gr(x: float):
    return x * 28.35

def gm_unc(x: float):
    return x / 28.35

def gal_lit(x: float):
    return x * 3.785

def lit_gal(x: float):
    return x / 3.785
def lit_pin(x: float):
    return x * 2
def pin_lit(x: float):
    return x / 2


dict ={1: djuim_sm, 2: sm_djuim, 3: miles_km, 4: km_miles, 5: funts_kg, 6: kg_funts, 7: unc_gr, 8: gm_unc, 9: gal_lit, 10: lit_gal, 11: lit_pin,12: pin_lit}
print(dict)
while True:
    y = int(input("Введите номер операции 1-12 :"))
    print(y)
    if y != 0:
        x = int(input("Введите значение для конвертирования: "))
        print(dict[y](x))
    else:
        break
