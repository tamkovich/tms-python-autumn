"""Написать 12 функций по переводу"""

def inch_to_cm(value: float) -> float:
    "method accept parametr value in inch and return value in cm"
    return value * 2.54


def cm_to_inch(value: float) -> float:
    "method accept parametr value in cm and return value in inch"
    return value / 2.54


def mile_to_km(value: float) -> float:
    "method accept parametr value in miles and return value in km"
    return value * 1.609


def km_to_mile(value: float) -> float:
    "method accept parametr value in km and return value in miles"
    return value / 1.609


def lbs_to_kg(value: float) -> float:
    "method accept parametr value in lbs and return value in kg"
    return value * 2.205


def kg_to_lbs(value: float) -> float:
    "method accept parametr value in kg and return value in lbs"
    return value / 2.205


def oz_to_gr(value: float) -> float:
    "method accept parametr value in oz and return value in gramms"
    return value * 28.35


def gr_to_oz(value: float) -> float:
    "method accept parametr value in grammes and return value in oz"
    return value * 0.03527


def gallons_to_lit(value: float) -> float:
    "method accept parametr value in gallons and return value in litres"
    return value * 3.785


def lit_to_gallons(value: float) -> float:
    "method accept parametr value in litres and return value in gallons"
    return value / 3.785


def pints_to_lit(value: float) -> float:
    "method accept parametr value in pints and return value in litres"
    return value * 1.76


def lit_to_pints(value: float) -> float:
    "method accept parametr value in litres and return value in pints"
    return value / 1.76