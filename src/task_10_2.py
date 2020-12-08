# Создать csv файл с данными о ежедневной погоде. Структура: Дата,
# Место, Градусы, Скорость ветра. Найти среднюю погоду(скорость ветра и
# градусы) для Минск за последние 7 дней.

import csv

with open('task_2.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    speed = []
    degr = []
    for row in csvreader:
        degr.append(row[2])
        speed.append(row[3])
    degr.pop(0)
    speed.pop(0)
    avg_speed = 0
    avg_degr = 0
    for value_speed in speed:
        avg_speed += int(value_speed)
    avg_speed /= len(speed)
    for value_degr in degr:
        avg_degr += int(value_degr)
    avg_degr /= len(degr)
    avg_speed = int(avg_speed)
    avg_degr = int(avg_degr)

print(f'Средняя температура и скорость ветра равны: {avg_degr} и {avg_speed}')
