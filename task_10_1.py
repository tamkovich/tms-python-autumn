# Создать csv файл с данными следующей структуры: Имя, Фамилия,
# Возраст. Создать отчетный файл с информацией по количеству людей
# входящих в ту или иную возрастную группу. Возрастные группы: 1-12, 13-18,
# 19-25, 26-40, 40+.
import csv
rows = [["Dmitry", "Korotsev", "39"],
        ["Mihail", "Medved", "29"],
        ["Leha", "Ivanov", "9"],
        ["Alex", "Moroz", "22"],
        ["Mahripa", "Ahripulaevna", "56"]]
filename = "Task_10_1.csv"
array = [
    ["1-12"],
    ["13-18"],
    ["19-25"],
    ["26-40"],
    ["40 +"]
]
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in rows:
        if  int(row[2]) <= 12 and int(row[2]) >= 1:
            array[0].append(row)
        elif int(row[2]) > 12 and int(row[2]) <= 18:
            array[1].append(row)
        elif int(row[2]) > 18 and int(row[2]) <= 25:
            array[2].append(row)
        elif int(row[2]) > 25 and int(row[2]) <= 40:
            array[3].append(row)
        elif int(row[2]) > 40:
            array[4].append(row)
with open('report.csv','w',newline = '') as csvfile:
    csvwriter = csv.writer(csvfile)
    for row in array:
        csvwriter.writerow(row)
