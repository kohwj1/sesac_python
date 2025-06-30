import module_a as ma

def start_program():
    print('main으로부터 호출된 start_program 함수')
    local_func_a()


def local_func_a():
    print('main으로부터 호출된 local_func_a 함수')
    ma.func_a1()


if __name__ == '__main__':
    start_program()