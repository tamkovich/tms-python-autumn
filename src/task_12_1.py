class MyTime:
    def __init__(self, *args):
        if len(args) == 3:
            print("на входе 3 значения")
            self.hours = int(args[0])
            self.minutes = int(args[1])
            self.seconds = int(args[2])
        elif not args:
            print("аргументы не переданы")
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
        elif type(args[0]) is str:
            print(f"На входе 1 значение в виде строки {args[0]}")
            a = args[0].split("-")
            self.hours = int(a[0])
            self.minutes = int(a[1])
            self.seconds = int(a[2])
        elif type(args[0]) is MyTime:
            print("На входе 1 значение в виде mytime")
            copy_time = args[0]
            self.hours = copy_time.hours
            self.minutes = copy_time.minutes
            self.seconds = copy_time.seconds

        if self.seconds > 59:
            self.seconds -= 60
            self.minutes += 1
        if self.minutes > 59:
            self.minutes -= 60
            self.hours += 1
        if self.hours > 23:
            self.hours -= 24
        if self.hours < 0:
            self.hours = 0
        if self.minutes < 0:
            self.minutes = 0
        if self.seconds < 0:
            self.seconds = 0

    @property
    def time_in_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def __eq__(self, other):
        return self.time_in_seconds == other.time_in_seconds

    def __ne__(self, other):
        return self.time_in_seconds != other.time_in_seconds

    def __add__(self, other):
        return self.time_in_seconds + other.time_in_seconds

    def __sub__(self, other):
        return self.time_in_seconds - other.time_in_seconds

    def __lt__(self, other):
        return self.time_in_seconds < other.time_in_seconds

    def __gt__(self, other):
        return self.time_in_seconds > other.time_in_seconds

    def __le__(self, other):
        return self.time_in_seconds <= other.time_in_seconds

    def __ge__(self, other):
        return self.time_in_seconds >= other.time_in_seconds

    def show(self):
        print(f"{self.hours}:{self.minutes}:{self.seconds}")


def time_in_iso(time):
    hour = time // 3600
    minute = (time - hour * 3600) // 60
    second = time - (hour * 3600 + minute * 60)
    return f"{hour}:{minute}:{second}"


time1 = MyTime(26, 65, 78)

time2 = MyTime("11-65-78")

time3 = MyTime(time1)
time4 = MyTime()

print(time1.hours)
print(time2.hours)
print(time3.hours)
print(time4.hours)

time1.show()
time2.show()
time3.show()
time4.show()

print(time_in_iso(time1 + time2))
