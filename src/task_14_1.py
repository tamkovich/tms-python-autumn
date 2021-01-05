"""Написать программу таймер. Программа при запуске принимает имя,
фамилию, часы, минуты и секунды. После программа начинает обратный
отсчет выводя оставшееся время. Программа должна хранить файл
логирования с информацией о том кто запускал программу и когда.
Пример ​ :
00:00:03
00:00:02
00:00:01
ALARM!!!"""

import argparse
from datetime import datetime
import time

now = datetime.now()
parser = argparse.ArgumentParser()
parser.add_argument("-fn", "--first-name", required=True)
parser.add_argument("-ln", "--last-name", required=True)
parser.add_argument("-hr", "--hours", required=True)
parser.add_argument("-mn", "--minutes", required=True)
parser.add_argument("-sc", "--seconds", required=True)
args = parser.parse_args()

with open("name.csv", "a") as csv_file:
    csv_file.write(args.first_name + "\n")
    csv_file.write(args.last_name + "\n")
    csv_file.write(str(now) + "\n")

end_time = int(args.hours) * 3600 + int(args.minutes) * 60 + int(args.seconds)

for i in range(end_time):
    end_time = end_time - 1
    print(time.strftime("%H:%M:%S", time.gmtime(end_time)))
    time.sleep(1)
print("ALARM!!!!!")

# python task_14_1.py -fn=anton -ln=sharypa -hr=0 -mn=0 -sc=50
