print("SELECT FUNCTION:\ninches to centimeters (1) \ncentimeters to inches (2) \n"
      "miles to kilometers (3) \nkilometers to miles (4) \nlb. to kilograms (5) "
      "\nkilograms to lb. (6) \nounce to grams (7) \n"
      "grams to ounce (8) \ngallons to liters (9) \nliters to gallons (10) \nUSA pints to liters (11) \n"
      "liters to USA pints (12) ")


# Дюймы в сантиметры (1)
def inch_to_cm(value_in_inches: int or float) -> int or float:
    """This method converts the value of inches to centimeters

    :param value_in_inches: int or float value in inch
    :return int or float value in centimeters
    """
    value_in_inches = value_in_inches * 2.54
    return value_in_inches


# Сантиметры в дюймы (2)
def cm_to_inch(value_in_cm: int or float) -> int or float:
    """This method converts the value of centimeters to inches

        :param value_in_cm: int or float value in centimeters
        :return int or float value in inches
    """
    value_in_cm = value_in_cm / 2.54
    return value_in_cm


# Мили в километры (3)
def mi_to_km(value_in_mi: int or float) -> int or float:
    """This method converts the value of miles to kilometers

        :param value_in_mi: int or float value in miles
        :return int or float value in kilometers
    """
    value_in_mi = value_in_mi * 1.60934
    return value_in_mi


# Километры в мили (4)
def km_to_mi(value_in_km: int or float) -> int or float:
    """This method converts the value of kilometers to miles

        :param value_in_km: int or float value in kilometers
        :return int or float value in miles
    """
    value_in_km = value_in_km / 1.60934
    return value_in_km


# Фунты в килограммы (5)
def lb_to_kg(value_in_lb: int or float) -> int or float:
    """This method converts the value of lb. to kilograms

        :param value_in_lb: int or float value in lb.
        :return int or float value in kilograms
    """
    value_in_lb = value_in_lb / 2.20462
    return value_in_lb


# Килограммы в фунтики (6)
def kg_to_lb(value_in_kg: int or float) -> int or float:
    """This method converts the value of kilograms to lb.

        :param value_in_kg: int or float value in kilograms
        :return int or float value in lb
    """
    value_in_kg = value_in_kg * 2.20462
    return value_in_kg


# Унции в граммы (7)
def ounce_to_grams(value_in_ounce: int or float) -> int or float:
    """This method converts the value of ounce to grams

        :param value_in_ounce: int or float value in ounce
        :return int or float value in grams
    """
    value_in_ounce = value_in_ounce * 28.3495
    return value_in_ounce


# Граммы в унции (8)
def grams_to_ounce(value_in_grams: int or float) -> int or float:
    """This method converts the value of grams to ounce

        :param value_in_grams: int or float value in grams
        :return int or float value in ounce
    """
    value_in_grams = value_in_grams / 28.3495
    return value_in_grams


# Галлон в литры (9)
def gallons_to_liters(value_in_gallons: int or float) -> int or float:
    """This method converts the value of gallons to liters

        :param value_in_gallons: int or float value in gallons
        :return int or float value in liters
    """
    value_in_gallons = value_in_gallons * 3.78541
    return value_in_gallons


# Литры в галлоны (10)
def liters_to_gallons(value_in_liters: int or float) -> int or float:
    """This method converts the value of liters to gallons

        :param value_in_liters: int or float value in liters
        :return int or float value in gallons
    """
    value_in_liters = value_in_liters / 3.78541
    return value_in_liters


# Пинты в литры (11)
def us_pints_to_liters(value_in_pints: int or float) -> int or float:
    """This method converts the value of USA pints to liters

        :param value_in_pints: int or float value in pints
        :return int or float value in liters
    """
    value_in_pints = value_in_pints * 0.473176
    return value_in_pints


# Литры в пинты (12)
def liters_to_us_pints(value_in_liters: int or float) -> int or float:
    """This method converts the value of liters to USA pints

        :param value_in_liters: int or float value in liters
        :return int or float value in USA pints.
    """
    value_in_liters = value_in_liters / 0.473176
    return value_in_liters


dict_of_function = [
    {'num': 1, "start": "Enter inches ", "end": " centimeters", "fun": inch_to_cm},
    {'num': 2, "start": "Enter centimeters ", "end": " inches", "fun": cm_to_inch},
    {'num': 3, "start": "Enter miles ", "end": " kilometers", "fun": mi_to_km},
    {'num': 4, "start": "Enter kilometers ", "end": " miles", "fun": km_to_mi},
    {'num': 5, "start": "Enter lb. ", "end": " kilograms", "fun": lb_to_kg},
    {'num': 6, "start": "Enter kilograms ", "end": " lb.", "fun": kg_to_lb},
    {'num': 7, "start": "Enter ounce ", "end": " grams", "fun": ounce_to_grams},
    {'num': 8, "start": "Enter grams ", "end": " ounce", "fun": grams_to_ounce},
    {'num': 9, "start": "Enter gallons ", "end": " liters", "fun": gallons_to_liters},
    {'num': 10, "start": "Enter liters ", "end": " gallons", "fun": liters_to_gallons},
    {'num': 11, "start": "Enter US pints ", "end": " liters", "fun": us_pints_to_liters},
    {'num': 12, "start": "Enter liters ", "end": " US pints", "fun": liters_to_us_pints},
]
print("________________________")
while True:
    number_fun = input("\nNumber of function: ")
    if number_fun.isdigit() != True:
        print("Enter int number!")
        continue
    number_fun = int(number_fun)
    if number_fun > 12 or number_fun < 0:
        print("ERROR OF NUMBER FUNCTIONS")
    if number_fun == 0:
        print("GOODBYE")
        break
    if 0 < number_fun <= 12:
        list_of_fun = dict_of_function[number_fun - 1]
        start_number = float(input(list_of_fun["start"]))
        fun = list_of_fun["fun"]
        finish_number = fun(start_number)
        print(round(finish_number, 3), (list_of_fun["end"]))
