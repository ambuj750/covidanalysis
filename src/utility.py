def convert_to_num(string):
    try:
        return int(string)
    except ValueError:
        return 0


def get_percentage():
    while True:
        try:
            percentage = int(input('Enter percentage: '))
            if percentage > 100 or percentage < 1:
                print('Please enter a number between 1 to 100.')
                continue
            else:
                return percentage
        except ValueError:
            print('Warning:Please enter a valid number format.')
            continue
