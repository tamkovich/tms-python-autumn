"""Создать список поездов. Структура словаря: номер поезда,
пункт и время прибытия, пункт и время отбытия. Вывести все сведения
 о поездах, время пребывания в пути которых превышает 7 часов 20 минут"""
import datetime

number_of_trains = input("enter number_of_trains ")
if number_of_trains.isdigit():
    number_of_trains = int(number_of_trains)
train_list = []
value = datetime.time(7, 20)
value_time = value.hour * 60 + value.minute
for i in range(number_of_trains):
    train_list.append(
        {
            "train_number": 1234,
            "point_of_departure": "Gomel",
            "point_of_arrival": "Minsk",
            "time_of_departure": datetime.time(
                int(input(f"hour departure {i+1} : ")),
                int(input(f"minutes departure {i+1} : ")),
            ),
            "time_of_arrival": datetime.time(
                int(input(f"hour arrival {i+1} : ")),
                int(input(f"minutes arrival {i+1} : ")),
            ),
        }
    )
print(train_list)
for i in train_list:
    if (i["time_of_arrival"].hour * 60 + i["time_of_arrival"].minute) - (
        i["time_of_departure"].hour * 60 + i["time_of_departure"].minute
    ) > value_time:
        print(f"train_number {i['train_number']}")
        print(f"point_of_departure {i['point_of_departure']}")
        print(f"point_of_arrival {i['point_of_arrival']}")
        print(f"time_of_departure {i['time_of_departure']}")
        print(f"time_of_arrival {i['time_of_arrival']}")
