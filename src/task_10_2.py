import csv

days = 7
with open("Weather.csv", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile)
    temp = 0
    row_count = 0
    wind_speed = 0
    for row in csvreader:
        row_count += 1
        temp += int(row[2])
        wind_speed += int(row[3])
        if row_count == days:
            break

    print("midlle temperature for 7 days: ", temp / row_count)
    print("midlle wind speed for 7 days: ", wind_speed / row_count)
