# exception 계층 공식문서: https://docs.python.org/3/library/exceptions.html

try:
    with open('hello.txt', 'r') as file:
        content = file.read()
    print(f'파일 내용:',content)
except FileNotFoundError:
    print('파일이 존재하지 않습니다.')
except IOError:
    print('파일을 읽을 수 없습니다.')
except:
    print('알 수 없는 오류입니다.')

