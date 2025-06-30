# https://docs.python.org/3.10/library/functions.html#open
file_path = 'text.txt'

with open(file_path,'r', encoding='UTF-8') as file:
#파일 경로, 읽어올 때의 모드 (r: 읽기, w:새로쓰기, a:이어서 쓰기) / windows의 경우 기본 인코딩이 cp949이므로 UTF-8 인코딩 옵션 필요
#with 블록이 끝나면 file이 자동으로 close된다
    content = file.read()

print('파일 내용:',content)