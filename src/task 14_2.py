import argparse
import datetime
import time


parser = argparse.ArgumentParser()
parser.add_argument("-fn", "--first-name", required=True)
parser.add_argument("-ln", "--last-name", required=True)
parser.add_argument("-tf", "--time-in-focus", default=5, type=int)
parser.add_argument("-tb", "--time-on-break", default=5, type=int)
parser.add_argument("-cc", "--count-cycle", default=4, type=int)
parser.add_argument("-nt", "--name-task", required=True)
args = parser.parse_args()

with open("timer.txt", "a") as file:
    file.write(args.first_name + ", ")
    file.write(args.last_name + ", ")
    file.write(str(args.time_in_focus) + ", ")
    file.write(str(args.time_on_break) + ", ")
    file.write(str(args.count_cycle) + ", ")
    file.write(args.name_task + ", ")
    file.write("Дата запуска: " + str(datetime.datetime.now()))
    file.write(" \n")


def pomodoro():
    for y in range(0, args.count_cycle):
        timer = args.time_in_focus
        print("Начинаем работу:" + str(datetime.timedelta(seconds=args.time_in_focus)))
        for i in range(0, args.time_in_focus):
            print(datetime.timedelta(seconds=timer))
            timer -= 1
            time.sleep(1)
        print("Начало перерыва: " + str(datetime.timedelta(seconds=args.time_on_break)))
        timer = args.time_on_break
        for x in range(0, args.time_on_break):
            print(datetime.timedelta(seconds=timer))
            timer -= 1
            time.sleep(1)


pomodoro()