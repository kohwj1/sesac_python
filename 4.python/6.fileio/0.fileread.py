# with 블록이 없던 시절의 파일 열고 닫기
file_path = 'text.txt'

#1. 파일 열기
file = open(file_path,'r')

#2. 파일 내용 읽어오기
content = file.read()

#3. 파일 닫기 --> 안 닫으면 메모리에 계속 상주하여 메모리 누수 발생 또는 정상적인 편집이 안 되는 문제 등이 있음
file.close()