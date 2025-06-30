#파이썬은 메소드 오버로딩을 지원하지 않음!

def test_echo():
    print('ㅎㅇ')


test_echo()
# test_echo('hi') --> 실행하면 오류남


def test_echo(echo):
    print(echo)

# test_echo() --> 실행하면 오류남
test_echo('hihi')