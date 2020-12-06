# Дюймы в сантиметры

def inch_to_cm(value_in_inches: int or float) -> int or float:
    """This method converts the value of inches to centimeters

    :param value_in_inches: int or float value in inch
    :return int or float value in centimeters
    """
    value_in_inches = value_in_inches * 2.54
    return value_in_inches


print(inch_to_cm(3.8))
