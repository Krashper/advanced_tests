def get_average():
    try:
        f = open("expections/numbers.txt")
        numbers = [int(value) for value in f]
        average = sum(numbers)/len(numbers)
        print(f'The average is: {average}')
    except FileNotFoundError:
        print('The file was not found.')
    except ValueError:
        print('The file has invalid data.')

get_average()