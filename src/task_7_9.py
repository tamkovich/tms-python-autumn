# Галлон в литры

def gallons_to_liters(value_in_gallons: int or float) -> int or float:
    """This method converts the value of gallons to liters

        :param value_in_gallons: int or float value in gallons
        :return int or float value in liters
    """
    value_in_gallons = value_in_gallons * 3.78541
    return value_in_gallons


print(gallons_to_liters(5))
