def cm2inch():
    cm1 = float(input('Enter amount in cm: '))
    inch1 = cm1 / 2.54
    return 'Inches:', inch1


def inch2cm():
    inch2 = float(input('Enter amount in inch : '))
    cm2 = inch2 * 2.54
    return 'Centimetres:', cm2


def ml2km():
    ml1 = float(input('Enter amount in miles : '))
    km1 = ml1 * 1.609
    return 'Kilometers: ', km1


def km2ml():
    km2 = float(input('Enter amount in kilometers : '))
    ml2 = km2 / 1.609
    return 'Miles: ', ml2


def pnd2kg():
    pnd1 = float(input('Enter amount in pounds : '))
    kg1 = pnd1 * 0.453
    return 'Kilograms:', kg1


def kg2pnd():
    kg2 = float(input('Enter amount on klgrms : '))
    pnd2 = kg2 / 0.453
    return 'Pounds: ', pnd2


def oz2gr():
    oz1 = float(input('Enter amount in ounces : '))
    gr1 = oz1 * 0.029
    return 'Grams: ', gr1


def gr2oz():
    gr2 = float(input('Enter amount in grams : '))
    oz2 = gr2 / 0.029
    return 'Ounces: ', oz2


def gal2ltr():
    gal1 = float(input('Enter amount in gallons : '))
    ltr1 = gal1 * 4.546
    return 'Liters: ', ltr1


def ltr2gal():
    ltr2 = float(input('Enter amount in liters : '))
    gal2 = ltr2 / 4.546
    return 'Gallons:', gal2


def pt2ltr():
    pt1 = float(input('Enter amount in pints : '))
    ltr3 = pt1 * 0.568
    return 'Liters: ', ltr3


def ltr2pt():
    ltr4 = float(input('Enter amount on liters : '))
    pt2 = ltr4 / 0.568
    return 'Pints: ', pt2


while True:
    print("""Pick one to convert:\n
          1-Centimeters to inches, 2- Inches to centimeters, \n
          3-Miles to kilometers ,4-Kilometers to miles, \n
          5-Pounds to kilograms, 6-Kilograms to pounds ,\n
          7-Ounces to grams ,8-Grams to ounces, \n
          9-Gallons to liters, 10-Liters to gallons ,\n
          11-Pints to liters ,12-Liters to pint.\n
           For exit type 0""")
    s = (input('Vvedite chislo ot 1 do 12 : '))
    if s == '0':
        break
    if s in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'):
        if s == '1':
            print(cm2inch())
        elif s == '2':
            print(inch2cm())
        elif s == '3':
            print(ml2km())
        elif s == '4':
            print(km2ml())
        elif s == '5':
            print(pnd2kg())
        elif s == '6':
            print(kg2pnd())
        elif s == '7':
            print(oz2gr())
        elif s == '8':
            print(gr2oz())
        elif s == '9':
            print(gal2ltr())
        elif s == '10':
            print(ltr2gal())
        elif s == '11':
            print(pt2ltr())
        elif s == '12':
            print(ltr2pt())
    else:
        print('\033[96mPick one from the list, please.\033[0m')
