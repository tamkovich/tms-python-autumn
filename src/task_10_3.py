"""Дан файл, содержащий различные даты. Каждая дата - это число, месяц и
год. Найти самую раннюю дату"""

from datetime import datetime
import csv

with open('CSV_fof_task_10_3.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    _list = []
    for row in csv_reader:
        _list.append(datetime.strptime(row[0], '%d.%m.%Y'))
print(min(_list))

csv_file.close()
