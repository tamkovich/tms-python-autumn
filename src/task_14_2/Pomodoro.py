import argparse
from func import focusing
from func import pause


parser = argparse.ArgumentParser()
parser.add_argument("-fn", "--first-name", required=True)
parser.add_argument("-ln", "--last-name", required=True)
parser.add_argument("-tf", "--time-focusing", default=1500, type=int)
parser.add_argument("-tb", "--time-break", default=300, type=int)
parser.add_argument("-cc", "--count-cycle", default=4, type=int)
parser.add_argument("-nt", "--name-task", required=True)
args = parser.parse_args()


def create_generator_pomodoro():
    for _ in range(0, args.count_cycle):
        with open("timer.txt", "a") as f:
            f.write(args.first_name + ", ")
            f.write(args.last_name + ", ")
            f.write(str(args.time_focusing) + ", ")
            f.write(str(args.time_break) + ", ")
            f.write(str(args.count_cycle) + ", ")
            f.write(args.name_task + " \n")
        args.count_cycle -= 1
        focusing()
        pause()


create_generator_pomodoro()
