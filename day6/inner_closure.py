# 전역 변수
level = 0

def outter():
    # 지역 변수
    level = 50

    def inner():
        # nonlocal 키워드를 사용하므로,
        # outter에 새로 정의된 지역변수 level 사용
        nonlocal level
        level += 3
        print(level)
    # return inner() : inner 함수의 호출 결과
    # 가 아닌 함수자체를 반환
    # 이때, outter 안쪽의 모든 환경을 포함해서 반환
    # 함수자체도 closuer를 갖는다!
    return inner

func = outter()
func()
func()
func()
func2 = outter()
func2()
func2()
func2()
print(id(func))
print(id(func2))
