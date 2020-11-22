# Мили в километры

def mi_to_km(value_in_mi: int or float) -> int or float:
    """This method converts the value of miles to kilometers

        :param value_in_mi: int or float value in miles
        :return int or float value in kilometers
    """
    value_in_mi = value_in_mi * 1.60934
    return value_in_mi


print(mi_to_km(10))
