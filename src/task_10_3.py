# Дан файл, содержащий различные даты. Каждая дата - это число, месяц и
# год. Найти самую раннюю дату.

import csv
from datetime import datetime
with open('task_3.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    x = []
    for row in csvreader:
        x.append(datetime.strptime(row[0], '%d.%m.%Y'))
print(min(x))
