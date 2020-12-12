"""Создать csv файл с данными следующей структуры: Имя, Фамилия,
Возраст. Создать отчетный файл с информацией по количеству людей
входящих в ту или иную возрастную группу. Возрастные группы: 1-12, 13-18,
19-25, 26-40, 40+."""

import csv

with open('CSV_fof_task_10_1.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=';')

    count_1_12 = 0
    count_13_18 = 0
    count_19_25 = 0
    cont_26_40 = 0
    count_40_ = 0

    for row in csv_reader:
        int_age = (int(row.get('age')))
        if 0 <= int_age <= 12:
            count_1_12 += 1
        elif 13 <= int_age <= 18:
            count_13_18 += 1
        elif 19 <= int_age <= 25:
            count_19_25 += 1
        elif 26 <= int_age <= 40:
            cont_26_40 += 1
        elif int_age > 40:
            count_40_ += 1

rows1 = [
    ['list(1-12 - ', count_1_12],
    ['13-18 - ', count_13_18],
    ['19-25 - ', count_19_25],
    ['26-40 - ', cont_26_40],
    ['40+ - ', count_40_]
]
filename = "count_of_ages_groups.csv"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter='\n')
    csvwriter.writerow(rows1)

csv_file.close()
