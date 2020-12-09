import datetime
train_list = [{'train_number':1, 'time_of_departure':datetime.time(3, 50), 'time_of_arrival':datetime.time(9, 40),\
               'departure_point':'Minsk', 'arrival_point': 'Moscow'},
              {'train_number':2, 'time_of_departure':datetime.time(4, 20), 'time_of_arrival':datetime.time(11, 40),\
               'departure_point':'Minsk', 'arrival_point': 'Moscow'},
              {'train_number':3, 'time_of_departure':datetime.time(1, 10), 'time_of_arrival':datetime.time(8, 40),\
               'departure_point':'Minsk', 'arrival_point': 'Moscow'}
              ]
value = datetime.time(7,20)
for i in train_list:
    if (i['time_of_arrival'].hour * 60 + i['time_of_arrival'].minute ) - \
            (i['time_of_departure'].hour * 60 + i['time_of_departure'].minute) > value.hour * 60 + value.minute:
        print(f"train_number {i['train_number']}")
        print(f"time_of_departure {i['time_of_departure']}")
        print(f"time_of_arrival {i['time_of_arrival']}")
        print(f"departure_point {i['departure_point']}")
        print(f"arrival_point {i['arrival_point']}")