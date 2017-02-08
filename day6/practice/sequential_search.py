def sequential_search(word, key):
    index = 0
    while word:
        if word[index] == key:
            return index 
        index += 1
    else:
        return 0

def search2(key, source):
    for index, char in enumerate(source):
        if char == key:
            return index
    return 0

result = sequential_search('legend', 'g')
print(result)

result2 = search2('g', 'legend')
print(result2)


