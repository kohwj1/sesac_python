try:
    result = 10 / 0 #크래시가 발생하여 실행 중단, 다음 줄 진행 불가
    print(result)
    #try 안의 범위는 최소화될 수록 좋다
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다')
    #except도 퉁치지 말고 구체적으로 핸들링할 수록 좋음

# 파이썬은 함수의 설명을 코드에 직접 입력할 떄 함수 안에 입력함
def convert_to_int(num_str):
    """글자를 숫자로 바꾸는 함수
    
    Args
        num_str(string): 사용자가 입력한 숫자 형태의 string
    Returns
        result: 숫자로 변환된 값. 변환에 실패 시 None를 리턴함
    """
    try:
        result = int(num_str)
    except ValueError:
        print('입력값이 숫자가 아닙니다. 올바른 숫자를 입력해주세요. 입력값:',num_str)
        result = None
    return result


def double_number(number):
    return number * 2
    



user_input = '23'
result = convert_to_int(user_input)

if result:
    result = double_number(convert_to_int(user_input))
    print(f'입력값 {user_input}의 두배는 {result}입니다.')