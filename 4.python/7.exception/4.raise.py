def square_root(num):
    if num < 0:
        print('음수는 제곱근을 구할 수 없습니다')
        return None
    return num ** 0.5

def square_root2(num):
    if num < 0:
        raise ValueError('음수의 제곱근은 계산할 수 없습니다')
    return num ** 0.5

try:
    print(square_root2(-1))
except ValueError as e:
    print(e)