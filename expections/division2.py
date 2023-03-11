def divide_by_zero_proof_division(dividend, divisor):
    try:
        return dividend/divisor
    except ZeroDivisionError:
        return 'Cannot divide by zero.'
    except TypeError:
        raise TypeError("Both arguments must be numbers.")

print(divide_by_zero_proof_division(10, 2))
print(divide_by_zero_proof_division(10, 0))
print(divide_by_zero_proof_division('10', 2))