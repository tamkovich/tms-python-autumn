# 1. Написать программу таймер. Программа при запуске принимает имя,
# фамилию, часы, минуты и секунды. После программа начинает обратный
# отсчет выводя оставшееся время. Программа должна хранить файл
# логирования с информацией о том кто запускал программу и когда.

import argparse
import time
import datetime


parser = argparse.ArgumentParser()
parser.add_argument("-fn", "--first-name", required=True)
parser.add_argument("-ln", "--last-name", required=True)
parser.add_argument("--hours", type=int, required=True)
parser.add_argument("--minutes", type=int, required=True)
parser.add_argument("--seconds", type=int, required=True)
args = parser.parse_args()

with open("timer.txt", "w") as f:
    f.write(args.first_name + ", ")
    f.write(args.last_name + ", ")
    f.write(str(datetime.datetime.now()))
    f.write(" \n")

time_in_seconds = args.hours * 3600 + args.minutes * 60 + args.seconds


def timer_generator():
    minute = args.minutes
    hour = args.hours
    seconds = args.seconds
    for i in range(0, time_in_seconds):
        print(f"{hour}:{minute}:{seconds - 1}")
        seconds -= 1
        time.sleep(1)
    print("Alarm!")


timer_generator()
