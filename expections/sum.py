def sum_from_files():
    try:
        with open("expections/numbers1.txt") as f1, open("expections/numbers2.txt") as f2:
            numbers1 = [int(line) for line in f1]
            numbers2 = [int(line) for line in f2]
            sum1 = sum(numbers1)
            sum2 = sum(numbers2)
            print("The sum of numbers in numbers1.txt is:", sum1)
            print("The sum of numbers in numbers2.txt is:", sum2)
    except FileNotFoundError:
        print('The file was not founded')
    except ValueError:
        print('The file has invalid data')
    except IndexError:
        print('You have IndexError')

sum_from_files()