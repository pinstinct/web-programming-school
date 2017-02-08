def print_argument_count(*args):
    args_count = len(args)
    print('args count: {}'.format(args_count))
    return args_count

result = print_argument_count(3, 4, 10, 'a', [])
print(result)
