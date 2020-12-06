"""Дан файл, содержащий различные даты. Каждая дата - это число, месяц и
год. Найти самую раннюю дату. [02-8.1-ML-29]"""
from datetime import datetime
import csv

with open("10_03.csv",'r') as csv_file:
    csvreader = csv.reader(csv_file)
    data = []
    for line in csvreader:
        data.append(datetime.strptime(line[0], "%d.%m.%Y"))
    print(f"The earliest date is {min(data)}")
