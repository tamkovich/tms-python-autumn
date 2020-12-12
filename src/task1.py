import argparse
import csv
from datetime import datetime
from func import timer

parser = argparse.ArgumentParser()
parser.add_argument("-fn", "--first-name", required=True)
parser.add_argument("-ln", "--last-name", required=True)
parser.add_argument("echo")

args = parser.parse_args()
new_list = [
    f"{args.first_name},{args.last_name},"
    f"{datetime.strftime(datetime.now(),'%H:%M:%S')}".split(",")
]
with open("test.csv", "a") as file:
    writer = csv.writer(file)
    for i in new_list:
        writer.writerow(i)
print(type(args.echo))
timer(args.echo)
