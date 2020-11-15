def santimeters_to_inch(num: int or float) -> int or float:
    """This method convert sintimeters to inch and print.

    :param num: some number
    """
    print(num * 2.54)


def inch_to_santimeters(num: int or float) -> int or float:
    """This method convert inch to santimeters and print.

    :param num: some number
    """
    print(num * 0.3937007874)


def mile_to_km(num: int or float) -> int or float:
    """This method convert mile to km and print.

    :param num: some number
    """
    print(num * 1.609344)


def km_to_mile(num: int or float) -> int or float:
    """This method convert km to mile and print.

    :param num: some number
    """
    print(num * 0.62137119224)


def ft_to_kg(num: int or float) -> int or float:
    """This method convert fount to kg and print.

    :param num: some number
    """
    print(num * 0.453592)


def kg_to_ft(num: int or float) -> int or float:
    """This method convert kg to fount and print.

    :param num: some number
    """
    print(num * 2.20462)


def unc_to_gramm(num: int or float) -> int or float:
    """This method convert unci to gramm and print.

    :param num: some number
    """
    print(num * 28.3495)


def gramm_to_unc(num: int or float) -> int or float:
    """This method convert gramm to unci and print.

    :param num: some number
    """
    print(num * 0.035274)


def gal_to_litr(num: int or float) -> int or float:
    """This method convert gallon to litr and print.

    :param num: some number
    """
    print(num * 3.78541)


def litr_to_gal(num: int or float) -> int or float:
    """This method convert litr to gallon and print.

    :param num: some number
    """
    print(num * 0.264172)


def pint_to_litr(num: int or float) -> int or float:
    """This method convert pinta to litr and print.

    :param num: some number
    """
    print(num * 0.5)


def litr_to_pint(num: int or float) -> int or float:
    """This method convert litr to pinta and print.

    :param num: some number
    """
    print(num * 2)


while True:
    case = input("enter number of point ")
    if case.isdigit():
        if case == "0":
            break
        number = input("enter number ")
        if number.isdigit():
            number = int(number)
            if case == "1":
                inch_to_santimeters(number)
            if case == "2":
                santimeters_to_inch(number)
            if case == "3":
                mile_to_km(number)
            if case == "4":
                km_to_mile(number)
            if case == "5":
                ft_to_kg(number)
            if case == "6":
                kg_to_ft(number)
            if case == "7":
                unc_to_gramm(number)
            if case == "8":
                gramm_to_unc(number)
            if case == "9":
                gal_to_litr(number)
            if case == "10":
                litr_to_gal(number)
            if case == "11":
                pint_to_litr(number)
            if case == "12":
                litr_to_pint(number)
    else:
        continue
