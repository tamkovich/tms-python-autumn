# Граммы в унции

def grams_to_ounce(value_in_grams: int or float) -> int or float:
    """This method converts the value of grams to ounce

        :param value_in_grams: int or float value in grams
        :return int or float value in ounce
    """
    value_in_grams = value_in_grams / 28.3495
    return value_in_grams


print(grams_to_ounce(100))
