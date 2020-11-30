# Дан файл, содержащий различные даты. Каждая дата - это число, месяц и
# год. Найти самую раннюю дату.
from datetime import datetime
import csv
array = [
['20.11.1982'],
['21.11.1857'],
['22.11.1872'],
['23.11.1991'],
['24.11.2020'],
['25.11.2020'],
['26.11.2020'],
['27.11.2020'],
['28.11.2020'],
['29.11.2020'],
['30.11.2020']
]
with open("kalendar.csv", 'w', newline = '') as csvfile:
    csvwriter = csv.writer(csvfile)
    for row in array:
        csvwriter.writerow(row)
with open("kalendar.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    list_date = []
    for row in csvreader:
        list_date.append(datetime.strptime(row[0],'%d.%m.%Y'))
print(min(list_date))


