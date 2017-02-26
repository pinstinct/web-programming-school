source = [9, 1, 6, 8, 4, 3, 2, 0, 5, 7]
length = len(source)

def selection_sort():
    for index in range(length-1):
        cur_min_index = index

        for inner_index in range(index+1, length):
            if source[cur_min_index] > source[inner_index]:
                cur_min_index = inner_index
        source[cur_min_index], source[index] = source[index], source[cur_min_index]

    print(source)

selection_sort()
