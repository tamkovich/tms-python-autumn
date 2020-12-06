# Фунты в килограммы

def lb_to_kg(value_in_lb: int or float) -> int or float:
    """This method converts the value of lb. to kilograms

        :param value_in_lb: int or float value in lb.
        :return int or float value in kilograms
    """
    value_in_lb = value_in_lb / 2.20462
    return value_in_lb


print(lb_to_kg(22))
