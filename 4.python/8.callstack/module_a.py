def func_a1():
    print('A모듈의 function_a1 호출')
    func_a2()

def func_a2():
    print('A모듈의 function_a2 호출')
    func_a3()

def func_a3():
    print('A모듈의 func_a3 함수 호출')
    test_1234()

def test_1234():
    print('A모듈의 test_1234 함수 호출')
    deep_call_1()

def deep_call_1():
    print('A모듈의 deep_call_1 함수 호출')
    raise RuntimeError('콜스택 확인용 에러')    

def call_test():
    print('나 A모듈 실행됨')

# call_test()
if __name__ == '__main__': #파이썬이 나를 직접 호출했을 때 실행되는 것
    call_test()