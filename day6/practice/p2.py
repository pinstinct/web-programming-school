def what_fruits(color):
    '''
    문자열 color 값을 매개변수로 받아
    문자열이 red면 apple,
    yellow면 banana,
    green이면 melon을 반환한다.
    어떤 경우도 아니라면 I don't know 반환
    '''
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
