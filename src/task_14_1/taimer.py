import argparse
import time


parser = argparse.ArgumentParser()
parser.add_argument("-fn", "--first-name", required=True)
parser.add_argument("-ln", "--last-name", required=True)
parser.add_argument("--hours", type=int)
parser.add_argument("--minutes", type=int)
parser.add_argument("--seconds", type=int)
args = parser.parse_args()

with open("timer.txt", "w") as f:
    f.write(args.first_name + ", ")
    f.write(args.last_name + ", ")
    f.write(str(args.hours) + ", ")
    f.write(str(args.minutes) + ", ")
    f.write(str(args.seconds) + " \n")

time_in_seconds = args.hours * 3600 + args.minutes * 60 + args.seconds


def timer_generator():
    minute = args.minutes
    hour = args.hours
    seconds = args.seconds
    for i in range(0, time_in_seconds):
        if hour == 0 and minute == 0 and seconds == 1:
            print("ALARM!")
            break
        elif 0 < seconds < 60:
            print(f"{hour}:{minute}:{seconds - 1}")
            seconds -= 1
            time.sleep(1)
        elif seconds == 0:
            seconds = 59
            minute -= 1
            print(f"{hour}:{minute}:{seconds - i}")
            time.sleep(1)
        elif minute == 0:
            hour -= 1
            minute = 60
            print(f"{hour}:{minute}:{seconds - i}")
            time.sleep(1)


timer_generator()
