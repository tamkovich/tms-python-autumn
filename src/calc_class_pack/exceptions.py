def get_valid_int_number():
    """FUnction which checks is it integer digit on enter or not."""
    while True:
        x = input()
        if x.isdigit():
            x = int(x)
            return x
        else:
            print('It is not integer. Put another value:')
            continue
