import csv


with open("Person.csv", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile)
    age1_12 = 0
    age13_18 = 0
    age19_25 = 0
    age26_40 = 0
    age40_plus = 0
    for row in csvreader:
        if int(row[2]) >= 1 and int(row[2]) <= 12:
            age1_12 += 1
        if int(row[2]) >= 13 and int(row[2]) <= 18:
            age13_18 += 1
        if int(row[2]) >= 19 and int(row[2]) <= 25:
            age19_25 += 1
        if int(row[2]) >= 26 and int(row[2]) <= 40:
            age26_40 += 1
        if int(row[2]) >= 40:
            age40_plus += 1


with open("report.txt", "w") as report:
    report.write("людей с возрастом от 1 до 12:")
    report.write(str(age1_12) + "\n")
    report.write("людей с возрастом от 13 до 18:")
    report.write(str(age13_18) + "\n")
    report.write("людей с возрастом от 19 до 25:")
    report.write(str(age19_25) + "\n")
    report.write("людей с возрастом от 26 до 40:")
    report.write(str(age26_40) + "\n")
    report.write("людей с возрастом от 40:")
    report.write(str(age13_18) + "\n")
