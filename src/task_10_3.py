# Дан файл, содержащий различные даты. Каждая дата - это число, месяц и
# год. Найти самую раннюю дату.

from datetime import datetime
import csv

with open("date.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    dates = []
    for line in csv_reader:
        dates.append(datetime.strptime(line[0], "%d.%m.%Y"))
print(min(dates))
