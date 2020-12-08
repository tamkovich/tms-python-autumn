import csv

fields = ["date", "month", "year"]
rows = [
    ["7:12:2020"],
    ["6:12:2020"],
    ["1:12:2019"],
    ["4:12:2020"],
    ["3:10:2019"],
    ["2:1:2020"],
    ["1:12:2020"],
]
filename = "date.csv"
with open(filename, "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

field2 = []
with open(filename, "r") as file:
    reader = csv.reader(file)
    fields = next(reader)
    for index, row in enumerate(reader):
        field2.append(row[0].split(":")[::-1])

print(field2)
min_date = field2[0]
print(f"min_date {min_date}")
for i in field2:
    for y in range(3):
        print(i, y)
        if int(i[y]) < int(min_date[y]):
            min_date = i
            print(f"min_date in for  {min_date}")
            break
        if int(i[y]) > int(min_date[y]):
            break

print(f"min_date last {min_date}")
