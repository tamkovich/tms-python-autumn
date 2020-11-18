"""Написать программу, со следующим интерфейсом: пользователю предоставляется на
выбор 12 вариантов перевода(описанных в первой задаче). Пользователь вводит цифру
от одного до двенадцати. После программа запрашивает ввести численное значение.
Затем программа выдает конвертированный результат. Использовать функции из первого
задания. Программа должна быть в бесконечном цикле. Код выхода из программы - “0”."""

import task_7_1

dict_of_functions = {
        "1": task_7_1.inch_to_cm,
        "2": task_7_1.cm_to_inch,
        "3": task_7_1.mile_to_km,
        "4": task_7_1.km_to_mile,
        "5": task_7_1.lbs_to_kg,
        "6": task_7_1.kg_to_lbs,
        "7": task_7_1.oz_to_gr,
        "8": task_7_1.gr_to_oz,
        "9": task_7_1.gallons_to_lit,
        "10": task_7_1.lit_to_gallons,
        "11": task_7_1.pints_to_lit,
        "12": task_7_1.lit_to_pints,
    }

def options():
    print("Choice, what you need, please? ")
    print(" 1. inch_to_cm\n 2. cm_to_inch.\n 3. mile_to_km.\n 4. km_to_mile.")
    print(" 5. lbs_to_kg.\n 6. kg_to_lbs.\n 7. oz_to_gr.\n 8. gr_to_oz. ")
    print(" 9. gallons_to_lit.\n 10. lit_to_gallons. \n 11. pints_to_lit.\n 12. lit_to_pints.")
    print(" 0. Cancel")

while True:
    options()
    choice = (input(" Enter the number, please:\n "))
    value = float(input())
    if choice == 0:
        break
    try:
        value = float(value)
    except TypeError:
        print("Try again.\n reccomend enter the NUMBER! ")
        continue
    if 0 < int(choice) <= 12:
        print(dict_of_functions[choice](value))
    else:
        print("Try again, number must be more than 0 and less than 13 ")
