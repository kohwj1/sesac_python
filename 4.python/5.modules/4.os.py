# https://docs.python.org/ko/3.10/library/os.html
import os

print('현재 작업 디렉토리는:',os.getcwd()) #현재 디렉토리 가져오기 (get current directory)
os.mkdir('폴더명') #폴더를 만들도록 OS에 요청하는 것
# os.mkdir('폴더명') #이미 존재하므로 실패: FileExistsError: [Errno 17] File exists: '폴더명'
print('생성 완료')

os.chdir('폴더명') #폴더명으로 이동
print(os.getcwd()) #현재 디렉토리 가져오기 (get current directory)

os.chdir('..')
print(os.getcwd()) #현재 디렉토리 가져오기 (get current directory)

os.rmdir('폴더명') #폴더를 삭제하도록
print('삭제 완료')
# os.rmdir('폴더명') #존재하지 않는 폴더 삭제 시도: FileNotFoundError: [Errno 2] No such file or directory: '폴더명'