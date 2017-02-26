def print_debug(func):
    def inner_func(*args, **kwargs):
        print('type(args) : {}'.format(type(args)))
        print('type(kwargs) : {}'.format(type(kwargs)))
        result = func(*args, **kwargs)
        return result
    return inner_func


@print_debug
def print_string(*args, **kwargs):
    print('print_string args {}, kwargs{}'.format(args, kwargs))
@print_debug
def print_int(*args, **kwargs):
    print('print_int args {}, kwargs {}'.format(args, kwargs))

print_string('a', 3929)
print_int(1, 2317289372187)
