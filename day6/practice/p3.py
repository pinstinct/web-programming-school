def square_or_multi(value1, value2=None):
    if value2 is None:
        return(value1 * value1)
    else:
        return(value1 * value2)

result1 = square_or_multi(3)
print(result1)

result2 = square_or_multi(5, 10)
print(result2)

result3 = square_or_multi(3, 3, 3)
print(result3)
