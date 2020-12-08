import csv

fields = ["date", "place", "degrees", "wind_speed"]
rows = [
    ["7:12:2020", "Minsk", "-6", "24"],
    ["6:12:2020", "Minsk", "0", "25"],
    ["5:12:2020", "Minsk", "2", "10"],
    ["4:12:2020", "Minsk", "-10", "12"],
    ["3:12:2020", "Minsk", "1", "13"],
    ["2:12:2020", "Minsk", "-4", "22"],
    ["1:12:2020", "Minsk", "-6", "15"],
]
filename = "pogoda.csv"
with open(filename, "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

with open(filename, "r") as file:
    reader = csv.reader(file)
    fields = next(reader)
    average_degrees = 0
    average_speed = 0
    for index, row in enumerate(reader):
        average_degrees += int(row[2])
        average_speed += int(row[3])
        if index == 6:
            average_degrees /= index + 1
            average_speed /= index + 1


print(average_degrees)
print(average_speed)
