def make_gugu():
    return [(lambda x, y : '{}x{}={}'.format(x, y, x*y))(x, y) for x in range(2, 10) for y in range(1, 10)]

result = make_gugu()
print(result)
