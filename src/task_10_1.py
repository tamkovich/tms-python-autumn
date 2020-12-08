import csv

fields = ["firstname", "lastname", "group"]
rows = [
    ["Alex", "noname", "90"],
    ["Max", "Ivanov", "21"],
    ["Igor", "Chvyrov", "18"],
    ["Zeka", "Zeka", "10"],
]
filename = "file_10_1.csv"
with open(filename, "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

rows2 = []
with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    print(csvreader)
    for row in csvreader:
        rows2.append(row)

print(rows2)

new_list = ["1-12", "13-18", "19 -25", "26-40", "40+"]
filename2 = "age.csv"
with open(filename2, "w") as f2:
    csvwriter = csv.writer(f2)
    for j in rows2:
        if int(j[2]) <= 12:
            csvwriter.writerow([new_list[0], j])
        elif int(j[2]) <= 18:
            csvwriter.writerow([new_list[1], j])
        elif int(j[2]) <= 25:
            csvwriter.writerow([new_list[2], j])
        elif int(j[2]) <= 40:
            csvwriter.writerow([new_list[3], j])
        elif int(j[2]) >= 40:
            csvwriter.writerow([new_list[4], j])
