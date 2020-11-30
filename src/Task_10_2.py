"""Создать csv файл с данными о ежедневной погоде. Структура: Дата,
Место, Градусы, Скорость ветра. Найти среднюю погоду(скорость ветра и
градусы) для Минск за последние 7 дней."""

import csv

with open("pogoda.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    temp = []
    wind = []

    for row in csvreader:
        temp.append(int(row[2]))
        wind.append(int(row[3]))
temp_reverse = temp[::-1]
wind_reverse = wind[::-1]
av_temp = sum(temp_reverse[0:7])/7
av_wind = sum(wind_reverse[0:7])/7
print(f'Средняя температура за 7 дней: {av_temp:.2}')
print(f'Средняя скорость ветра за 7 дней: {av_wind:.2}')

