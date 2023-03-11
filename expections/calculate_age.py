from datetime import date

def calculate_age(year_of_birth):
    now_year = date.today().year
    if year_of_birth <= 0:
        raise ValueError('Birth year must be a positive integer.')
    return now_year - year_of_birth

print(calculate_age(2000))