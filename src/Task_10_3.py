"""Дан файл, содержащий различные даты. Каждая дата - это число, месяц и
год. Найти самую раннюю дату."""


from datetime import datetime
import csv

with open("Dates.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    arr = []
    for row in csvreader:
        arr.append(datetime.strptime(row[0], '%d.%m.%Y'))
print(min(arr))
