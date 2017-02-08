def what_fruits(color):
    if color == 'red':
        return 'apple'
    elif color == 'yellow':
        return 'banana'
    elif color == 'green':
        return 'melon'
    else:
        return 'I don\'t know'

result1 = what_fruits('red')
print(result1)

result2 = what_fruits('yellow')
print(result2)

result3 = what_fruits('green')
print(result3)

result4 = what_fruits('black')
print(result4)
