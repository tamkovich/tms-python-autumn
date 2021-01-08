"""На вход программа получает имя, фамилию, время для
фокусировки(по-умолчанию 25 минут), длину перерыва(по-умолчанию 5 минут),
количество циклов(по-умолчанию 4) и название задачи. Программа указывает
оставшееся время фокусировки, после сигнализирует о наступлении перерыва,
после сигнализирует о начале нового цикла фокусировки. Программа должна
вести файл лога о всех запусках."""

import argparse
from datetime import datetime
import os
import time


now = datetime.now()
parser = argparse.ArgumentParser()
parser.add_argument("-fn", "--first-name", required=True)
parser.add_argument("-ln", "--last-name", required=True)
parser.add_argument("-ft", "--focus-time", required=True)
parser.add_argument("-bt", "--break-time", required=True)
parser.add_argument("-aoc", "--amount-of-cicles", required=True)
parser.add_argument("-tn", "--task-name", required=True)
args = parser.parse_args()

with open("pomodoro.csv", "a") as csv_file:
    csv_file.write(args.first_name + "\n")
    csv_file.write(args.last_name + "\n")
    csv_file.write(args.focus_time + "\n")
    csv_file.write(args.break_time + "\n")
    csv_file.write(args.amount_of_cicles + "\n")
    csv_file.write(args.task_name + "\n")
    csv_file.write(str(now) + "\n")

focus_time_seconds = int(args.focus_time) * 60
break_time_seconds = int(args.break_time) * 60
count = int(args.amount_of_cicles)

for z in range(count):
    for i in range(focus_time_seconds):
        focus_time_seconds = focus_time_seconds - 1
        print(time.strftime("%H:%M:%S", time.gmtime(focus_time_seconds)))
        time.sleep(1)
    print("Перерыв")
    os.system('spd-say "Time to rest"')
    for h in range(break_time_seconds):
        break_time_seconds = break_time_seconds - 1
        print(time.strftime("%H:%M:%S", time.gmtime(break_time_seconds)))
        time.sleep(1)
    print("За работу")
    os.system('spd-say "Time to work"')
    focus_time_seconds = int(args.focus_time) * 60
    break_time_seconds = int(args.break_time) * 60
os.system('spd-say "All cycles finished"')


# python task_14_2.py -fn=anton -ln=sharypa -ft=0.5 -bt=0.5 -aoc=4 -tn=studybr
