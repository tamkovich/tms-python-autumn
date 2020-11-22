# Километры в мили

def km_to_mi(value_in_km: int or float) -> int or float:
    """This method converts the value of kilometers to miles

        :param value_in_km: int or float value in kilometers
        :return int or float value in miles
    """
    value_in_km = value_in_km / 1.60934
    return value_in_km


print(km_to_mi(10))
