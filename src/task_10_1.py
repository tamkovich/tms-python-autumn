#Создать csv файл с данными следующей структуры: Имя, Фамилия,
#Возраст. Создать отчетный файл с информацией по количеству людей
#входящих в ту или иную возрастную группу. Возрастные группы: 1-12, 13-18,
#19-25, 26-40, 40+.
import csv

category = [
    ["1 - 12"],
    ["13 - 18"],
    ["19 - 25"],
    ["26 - 40"],
    ["40 +"]
]
with open('otchet.csv') as csv_file: # считывает и преобразует файл
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        if int(line[-1]) <= 12:
            category[0].append(f"Name: {line[0]}, Surname: {line[1]}, Age: {line[2]}")
        elif int(line[-1]) < 19 and int(line[-1]) > 12:
            category[1].append(f"Name: {line[0]}, Surname: {line[1]}, Age: {line[2]}")
        elif int(line[-1]) < 26 and int(line[-1]) > 18:
            category[2].append(f"Name: {line[0]}, Surname: {line[1]}, Age: {line[2]}")
        elif int(line[-1]) < 41 and int(line[-1]) > 25:
            category[3].append(f"Name: {line[0]}, Surname: {line[1]}, Age: {line[2]}")
        else:
            category[4].append(f"Name: {line[0]}, Surname: {line[1]}, Age: {line[2]}")

print(category)


def csv_writer(category, path):
    with open(path, "w", newline='') as csv1_file:
        writer = csv.writer(csv1_file, delimiter=',')
        for line1 in category:
            writer.writerow(line1)
            
path = "new_otchet.csv"
csv_writer(category, path)