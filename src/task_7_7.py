# Унции в граммы

def ounce_to_grams(value_in_ounce: int or float) -> int or float:
    """This method converts the value of ounce to grams

        :param value_in_ounce: int or float value in ounce
        :return int or float value in grams
    """
    value_in_ounce = value_in_ounce * 28.3495
    return value_in_ounce


print(ounce_to_grams(10.5))
