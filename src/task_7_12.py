# Литры в пинты

def liters_to_us_pints(value_in_liters: int or float) -> int or float:
    """This method converts the value of liters to USA pints

        :param value_in_liters: int or float value in liters
        :return int or float value in USA pints.
    """
    value_in_liters = value_in_liters / 0.473176
    return value_in_liters


print(liters_to_us_pints(3))
