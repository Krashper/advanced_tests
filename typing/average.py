from typing import List, Union

def average(numbers: List[Union[float, int]]) -> Union[float, str]:
    try:
        if not numbers:
            return 'Cannot calculate the average of an empty list.'
        return sum(numbers) / len(numbers)
    except TypeError:
        raise TypeError("All elements in the list must be numbers.")

print(average([1, 2, 3, 4, 5]))
print(average([]))
print(average([1, '2', 3]))