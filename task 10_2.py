# Создать csv файл с данными о ежедневной погоде. Структура: Дата,
# Место, Градусы, Скорость ветра. Найти среднюю погоду(скорость ветра и
# градусы) для Минск за последние 7 дней.
import csv
array = [
['20.11.2020', 'Minsk', 4, 4],
['21.11.2020', 'Minsk', 3, 2],
['22.11.2020', 'Minsk', 2, 7],
['23.11.2020', 'Minsk', 5, 6],
['24.11.2020', 'Minsk', 5, 6],
['25.11.2020', 'Minsk', 7, 3],
['26.11.2020', 'Minsk', 1, 4],
['27.11.2020', 'Minsk', 1, 4],
['28.11.2020', 'Minsk', 0, 0],
['29.11.2020', 'Minsk', 0, 3],
['30.11.2020', 'Minsk', 0, 3]
]
with open("pogoda.csv", 'w', newline = '') as csvfile:
    csvwriter = csv.writer(csvfile)
    for row in array:
        csvwriter.writerow(row)

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
