# Литры в галлоны

def liters_to_gallons(value_in_liters: int or float) -> int or float:
    """This method converts the value of liters to gallons

        :param value_in_liters: int or float value in liters
        :return int or float value in gallons
    """
    value_in_liters = value_in_liters / 3.78541
    return value_in_liters


print(liters_to_gallons(5))
