#Создать csv файл с данными о ежедневной погоде. Структура: Дата,
#Место, Градусы, Скорость ветра. Найти среднюю погоду(скорость ветра и
#градусы) для Минск за последние 7 дней.

import csv

temp = []
speed = []
count = 0
couns = 0


with open('temp.csv') as csv_file: # считывает файл
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        temp.append(line[2])
        speed.append(line[3])
    for i in range(len(temp)):
        count += int(temp[i])
    for s in range(len(speed)):
        couns += int(speed[s])
    print(f"Средняя температура равна {count/len(temp)} градусов")
    print(f"Средняя скорость ветра равна {couns/len(speed)} метров")


