# Сантиметры в дюймы

def cm_to_inch(value_in_cm: int or float) -> int or float:
    """This method converts the value of centimeters to inches

        :param value_in_cm: int or float value in centimeters
        :return int or float value in inches
    """
    value_in_cm = value_in_cm / 2.54
    return value_in_cm


print(cm_to_inch(1))
