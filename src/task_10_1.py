# Создать csv файл с данными следующей структуры: Имя, Фамилия,
# Возраст. Создать отчетный файл с информацией по количеству людей
# входящих в ту или иную возрастную группу. Возрастные группы: 1-12, 13-18,
# 19-25, 26-40, 40+.

import csv

otchet = [
    ['1-12'],
    ['13-18'],
    ['19-25'],
    ['26-40'],
    ['40+']
]

with open('task_1.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        if int(row[2]) <= 12:
            otchet[0].append(f'{row[0]} {row[1]} {row[2]}')
        elif 13 <= int(row[2]) <= 18:
            otchet[1].append(f'{row[0]} {row[1]} {row[2]}')
        elif 19 <= int(row[2]) <= 25:
            otchet[2].append(f'{row[0]} {row[1]} {row[2]}')
        elif 26 <= int(row[2]) <= 40:
            otchet[3].append(f'{row[0]} {row[1]} {row[2]}')
        elif int(row[2]) > 40:
            otchet[4].append(f'{row[0]} {row[1]} {row[2]}')


def csv_writer(otchet, path):
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in otchet:
            writer.writerow(line)


path = "otchet.csv"
csv_writer(otchet, path)
