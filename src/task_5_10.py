"""10) Создать список поездов. Структура словаря: номер поезда,
пункт и время прибытия, пункт и время отбытия.
Вывести все сведения о поездах,
время пребывания в пути которых превышает
7 часов 20 минут.[02-7.3-ML02]"""

import datetime

poezda = {
    "422": {
        "Номер поезда": "422",
        "Пункт отбытия": "Лепель",
        "Время отбытия": "02:00:00",
        "Пункт прибытия": "Гродно",
        "Время прибытия": "14:20:00",
    },
    "244": {
        "Номер поезда": "244",
        "Пункт отбытия": "Варшава",
        "Время отбытия": "01:00:00",
        "Пункт прибытия": "Могилев",
        "Время прибытия": "06:40:00",
    },
    "345": {
        "Номер поезда": "345",
        "Пункт отбытия": "Минск",
        "Время отбытия": "06:00:00",
        "Пункт прибытия": "Санкт-Петербург",
        "Время прибытия": "10:30:00",
    },
}
for keys, value in poezda.items():
    x = value.get("Время отбытия").split()
    y = value.get("Время прибытия").split()

    for i in x:
        ho = i[0:2]
        mo = i[3:5]
        if ho.isdigit() and mo.isdigit():
            ho = int(ho)
            mo = int(mo)
        for m in y:
            hp = m[0:2]
            mp = m[3:5]
            if hp.isdigit() and mp.isdigit():
                hp = int(hp)
                mp = int(mp)
            for values in poezda.items():
                pribitie = datetime.timedelta(hours=hp, minutes=mp)
                otpravlenie = datetime.timedelta(hours=ho, minutes=mo)
                raznica = datetime.timedelta(hours=7, minutes=20)
    if otpravlenie + raznica < pribitie:
        print(value)
