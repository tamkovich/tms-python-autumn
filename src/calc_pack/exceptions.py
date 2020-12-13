def exc3ption():
    while True:
        x = input()
        if x.isdigit():
            x = int(x)
            return x
        else:
            print('It is not integer. Put another value:')
            continue
