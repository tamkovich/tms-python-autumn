import csv
from datetime import datetime

with open("Date.csv", encoding="utf-8") as csvfile:

    csvreader = csv.reader(csvfile)
    date = []
    for row in csvreader:
        date.append(datetime.strptime(row[0], "%d.%m.%Y"))

print(min(date))
