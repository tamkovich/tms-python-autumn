"""Написать 12 функций по переводу"""

def inch_to_cm(value: float) -> float:
    """This method sum 2 values
       :return sum of number `a` and `b`
       """
    return value * 2.54+ "cm "


def cm_to_inch(value: float) -> float:
    return value / 2.54


def mile_to_km(value: float) -> float:
    return value * 1.609


def km_to_mile(value: float) -> float:
    return value / 1.609


def lbs_to_kg(value: float) -> float:
    return value * 2.205


def kg_to_lbs(value: float) -> float:
    return value / 2.205


def oz_to_gr(value: float) -> float:
    return value * 28.35


def gr_to_oz(value: float) -> float:
    return value * 0.03527


def gallons_to_lit(value: float) -> float:
    return value * 3.785


def lit_to_gallons(value: float) -> float:
    return value / 3.785


def pints_to_lit(value: float) -> float:
    return value * 1.76


def lit_to_pints(value: float) -> float:
    return value / 1.76