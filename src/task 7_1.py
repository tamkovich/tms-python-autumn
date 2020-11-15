#Написать 12 функций по переводу:
#1. Дюймы в сантиметры
#2. Сантиметры в дюймы
#3. Мили в километры
#4. Километры в мили
#5. Фунты в килограммы
#6. Килограммы в фунты
#7. Унции в граммы
#8. Граммы в унции
#9. Галлон в литры
#10. Литры в галлоны
#11. Пинты в литры
#12. Литры в пинты

def djuim_sm(x: float):
    return x * 2.54
djuim = djuim_sm(1)
print(djuim)

def sm_djuim(x: float):
    return x / 2.54
sm = sm_djuim(1)
print(sm)


def miles_km(x: float):
    return x * 1.609
mile = miles_km(1)
print(mile)

def km_miles(x: float):
    return x / 1.609
km = km_miles(1)
print(km)

def funts_kg(x: float):
    return x / 2.2046
funts = funts_kg(1)
print(funts)

def kg_funts(x: float):
    return x * 2.2046
kg = kg_funts(1)
print(kg)

def unc_gr(x: float):
    return x * 28.35
unc = unc_gr(1)
print(unc)

def gm_unc(x: float):
    return x / 28.35
gm = gm_unc(1)
print(gm)

def gal_lit(x: float):
    return x * 3.785
gal = gal_lit(1)
print(gal)

def lit_gal(x: float):
    return x / 3.785
lit = lit_gal(1)
print(lit)

def lit_pin(x: float):
    return x * 2
lit = lit_pin(1)
print(lit)

def pin_lit(x: float):
    return x / 2
pin = pin_lit(1)
print(pin)
