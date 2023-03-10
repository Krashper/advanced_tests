def convert_to_int(string):
    try:
        return int(string)
    except ValueError:
        return 'This string cannot be converted'


print(convert_to_int('123'))
print(convert_to_int('hi'))