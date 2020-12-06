class MyTime:
    def __init__(self, *args, **kwargs):
        if len(args) == 3:
            print("На входе 3 значения")
            self.hours = args[0]
            self.minutes = args[1]
            self.seconds = args[2]
        elif type(args[0]) is str:
            print(f"На входе 1 значение в виде строки: {args[0]}")
            arr = args[0].split('-')
            self.hours = int(arr[0])
            self.minutes = int(arr[1])
            self.seconds = int(arr[2])
        elif type(args[0]) is MyTime:
            print("На входе 1 значение в виде MyTime")
            copy_time = args[0]
            self.hours = copy_time.hours
            self.minutes = copy_time.minutes
            self.seconds = copy_time.seconds
        elif args == ():
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
        while True:
            if self.seconds > 59:
                self.seconds -= 60
                self.minutes += 1
                if self.minutes >= 60:
                    self.minutes -= 60
                    self.hours += 1
                    if self.hours > 23:
                        self.hours -= 24

    @property
    def time_in_seconds(self):
        hours_time_in_seconds = self.hours * 3600
        minutes_time_in_seconds = self.minutes * 60
        return self.seconds + minutes_time_in_seconds + hours_time_in_seconds

    def __eq__(self, other: 'MyTime') -> bool:
        return self.time_in_seconds == other.time_in_seconds

    def __ne__(self, other: 'MyTime') -> bool:
        return self.time_in_seconds > other.time_in_seconds

    def __lt__(self, other: 'MyTime') -> bool:
        return self.time_in_seconds > other.time_in_seconds

    def __gt__(self, other: 'MyTime') -> bool:
        return self.time_in_seconds < other.time_in_seconds

    def __le__(self, other: 'MyTime') -> bool:
        return self.time_in_seconds >= other.time_in_seconds

    def __ge__(self, other: 'MyTime') -> bool:
        return self.time_in_seconds >= other.time_in_seconds

    def __add__(self, other: 'MyTime') -> bool:
        return self.time_in_seconds + other.time_in_seconds

    def __sub__(self, other: 'MyTime') -> bool:
        return self.time_in_seconds - other.time_in_seconds

    def __mul__(self, other: 'MyTime') -> bool:
        return self.time_in_seconds * other

    def show_results(self):
        return f'{self.hours}:{self.minutes}:{self.seconds}'
