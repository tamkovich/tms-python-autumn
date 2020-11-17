# Создать список поездов. Структура словаря: номер поезда,
# пункт и время прибытия, пункт и время отбытия. Вывести все сведения о поездах,
# время пребывания в пути которых превышает 7 часов 20 минут.

import datetime

train_list = [
    {'train_number': 1, 'time_of_departure': datetime.time(3, 50),
     'time_of_arrival': datetime.time(6, 20)
     },
    {'train_number': 2, 'time_of_departure': datetime.time(3, 40),
     'time_of_arrival': datetime.time(10, 15)
     },
    {'train_number': 3, 'time_of_departure': datetime.time(1, 10),
     'time_of_arrival': datetime.time(8, 55)
     },
    {'train_number': 4, 'time_of_departure': datetime.time(2, 38),
     'time_of_arrival': datetime.time(18, 12)
     },
]
value = datetime.time(7, 20)
value_in_minutes = value.hour * 60 + value.minute
for i in train_list:
    if (i["time_of_arrival"].hour * 60 + i["time_of_arrival"].minute) - \
            (i["time_of_departure"].hour * 60 + i["time_of_departure"].minute) > value_in_minutes:
        a = (i["time_of_arrival"].hour * 60 + i["time_of_arrival"].minute) - \
            (i["time_of_departure"].hour * 60 + i["time_of_departure"].minute)
        print()
        print("Time in way: ", a)
        print(f"train_number {i['train_number']}")
