"""Создать csv файл с данными следующей структуры: Имя, Фамилия,
Возраст. Создать отчетный файл с информацией по количеству людей
входящих в ту или иную возрастную группу. Возрастные группы: 1-12, 13-18,
19-25, 26-40, 40+."""

import csv

group_of_ages = [
    ['1-12'],
    ['13-18'],
    ['19-25'],
    ['26-40'],
    ['40+']
]

def print_csv_file(filename):
    with open(f"{filename}.csv") as my_file:
        for line in my_file.readlines():
            print(line)

def csv_writer(final_file, name_of_file):
    with open(name_of_file, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in final_file:
            writer.writerow(line)

def check_group_of_ages(filename, final_file):
    with open(f"{filename}.csv") as my_file:
        csvreader = csv.reader(my_file)
        for row in csvreader:
            if int(row[2]) <= 12:
                final_file[0].append(f'{row[0]} {row[1]} {row[2]}')
            elif 13 <= int(row[2]) <= 18:
                final_file[1].append(f'{row[0]} {row[1]} {row[2]}')
            elif 19 <= int(row[2]) <= 25:
                final_file[2].append(f'{row[0]} {row[1]} {row[2]}')
            elif 26 <= int(row[2]) <= 40:
                final_file[3].append(f'{row[0]} {row[1]} {row[2]}')
            else:
                final_file[4].append(f'{row[0]} {row[1]} {row[2]}')

    return final_file


print_csv_file("task_10_1")
csv_writer(group_of_ages, "final_file")
print(check_group_of_ages("task_10_1", group_of_ages))
