def print_debug(func):
    def inner_func(*args, **kwargs):
        # id가 동일하게 출력되는건 왜지...?
        print('id(args) : {}'.format(type(args)))
        print('id(kwargs) : {}'.format(type(kwargs)))
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
