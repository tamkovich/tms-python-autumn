"""Создать csv файл с данными о ежедневной погоде. Структура: Дата,
Место, Градусы, Скорость ветра. Найти среднюю погоду(скорость ветра и
градусы) для Минск за последние 7 дней."""

import csv

list_of_speed = []
list_of_degr = []

def print_csv_file(filename):
    with open(f"{filename}.csv") as my_file:
        for line in my_file.readlines():
            print(line)

def open_file_for_read_and_data_collection(filename:str, list_of_speed, list_of_degr:list):
    with open(f"{filename}.csv") as my_file:
        csvreader = csv.reader(my_file)
        for line in csvreader:
            list_of_degr.append(line[2])
            list_of_speed.append(line[3])
        result_of_speed = list(map(int, list_of_speed))
        result_of_degr = list(map(int, list_of_degr))
    return result_of_speed, result_of_degr

def calculate_average(value:list) -> str:
    return f"The average value is {sum(value) / len(value)}"


result_of_speed, result_of_degr = open_file_for_read_and_data_collection("10_02", list_of_speed, list_of_degr)
print_csv_file("10_02")
open_file_for_read_and_data_collection("10_02", list_of_speed, list_of_degr)
print(calculate_average(result_of_speed), calculate_average(result_of_degr))
