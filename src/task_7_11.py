# Пинты в литры

def us_pints_to_liters(value_in_pints: int or float) -> int or float:
    """This method converts the value of USA pints to liters

        :param value_in_pints: int or float value in pints
        :return int or float value in liters
    """
    value_in_pints = value_in_pints * 0.473176
    return value_in_pints


print(us_pints_to_liters(5))
