# Килограммы в фунтики

def kg_to_lb(value_in_kg: int or float) -> int or float:
    """This method converts the value of kilograms to lb.

        :param value_in_kg: int or float value in kilograms
        :return int or float value in lb
    """
    value_in_kg = value_in_kg * 2.20462
    return value_in_kg


print(kg_to_lb(50))