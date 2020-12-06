def convertor(_type: int, x: float):
    arr = {1: duim_sm,
           2: sm_duim,
           3: miles_km,
           4: km_miles,
           5: funts_kg,
           6: kg_funts,
           7: unc_gr,
           8: gm_unc,
           9: gal_lit,
           10: lit_gal,
           11: lit_pin,
           12: pin_lit}
    print(arr[_type](x))
    while True:
        _type = int(input("Введите тип новой операции"))
        if _type != 0:
            x = int(input("Введите новое значение"))
            print(arr[_type](x))
        else:
            break


def duim_sm(x: float):
    return x * 2.54


def sm_duim(x: float):
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


convertor(1, 2)
