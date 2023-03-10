def find_file():
    file_name = input('Enter the name of the file: ')
    try:
        with open(file_name, 'r') as f:
            print('It is work')
    except FileNotFoundError:
        print(f'File with name {file_name} not found')

find_file()
find_file()