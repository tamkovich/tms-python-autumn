"""Создать csv файл с данными о ежедневной погоде. Структура: Дата,
Место, Градусы, Скорость ветра. Найти среднюю погоду(скорость ветра и
градусы) для Минск за последние 7 дней."""

import csv

summ_value_speed = 0
summ_value_temp = 0
average_of_days = 7

with open('CSV_file_for_task_10_2.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=';')
    for row in csv_reader:
        value_speed = (int(row.get('speed')))
        summ_value_speed += value_speed
        value_temp = (int(row.get('temp')))
        summ_value_temp += value_temp

print('average speed of ', average_of_days, 'days ', 'is ',
      round(summ_value_speed / average_of_days, 2))
print('average temp of ', average_of_days, 'days ', 'is ',
      round(summ_value_temp / average_of_days, 2))

csv_file.close()
