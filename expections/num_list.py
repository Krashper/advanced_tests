def num_list():
    try:
        user_input = input('Enter a list of numbers separated by commas: ')
        nums = [int(i) for i in user_input.split(',')]
        return nums
    except ValueError:
        return 'You entered the string incorrectly. Please enter only numbers separated by commas :)'

print(num_list())