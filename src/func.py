import time


def timer(a: str):
    """Function timer.

    The function prints the time to the console with a
    period of one second.
    """
    li = a.split(":")
    for i in range(3):
        li[i] = int(li[i])

    number_second = 3600 * li[0] + 60 * li[1] + li[2]

    for time_in_sec in range(1, number_second + 1)[::-1]:
        hour = time_in_sec // 3600
        minute = (time_in_sec - hour * 3600) // 60
        second = time_in_sec - (hour * 3600 + minute * 60)
        print(f"{hour}:{minute}:{second}")
        time.sleep(1)

    print("ALARMS!!!!")
