def print_args(func):
    def inner_func(*args, **kwargs):
        print('args : {}'.format(args))
        result = func(*args, **kwargs)
        return result
    return inner_func

def decorate_test(func):
    def inner_func(*args, **kwargs):
        print('test_inner_func')
        return func(*args, **kwargs)
    return inner_func

# 데코레이터 사용
# 데코레이터를 여러개 사용할 경우,
# 함수에서 가장 가까운 것 부터 실행
@print_args
@decorate_test
def multi(arg1, arg2):
    # 똑같은 기능을 하는 부분
    # print('args : {}, {}'.format(arg1, arg2))
    result = arg1 * arg2
    print(result)
    return result

@decorate_test
@print_args
def divide(arg1, arg2):
    # print('args : {}, {}'.format(arg1, arg2))
    result = arg1 / arg2
    print(result)
    return result

multi(3, 5)
divide(10, 2)

func1 = decorate_test(multi)
func1(100, 2)
func2 = print_args(divide)
func2(200, 2)
