def extract_from_dict(dict):
    try:
        key = input('Enter key for dictionary: ')
        return dict[key]
    except KeyError:
        return "Dictionary doesn't have that key"

my_dict = {'length': 5, 'id': '1234'}
print(extract_from_dict(my_dict))