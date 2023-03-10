def division(dividend, divisor):
    try:
        quotient = dividend/divisor
        return quotient
    except ZeroDivisionError:
        return 'Cannot divide by zero'

print(division(4, 2))
print(division(10, 0))
