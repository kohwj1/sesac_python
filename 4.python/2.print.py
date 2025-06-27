name = 'Alice'

print(name)
print('Hello,' , name) #콤마로 구분 시 중간에 공백 추가됨 (argument로 받은 값)
print('Hello,' + name+'!!') #더하기 연산이므로 중간 공백 없음

name1 = 'Bob'
name2 = 'Charlie'

print('Hello, {1}!! {0}'.format(name1, name2)) #python 3.x 초창기..., 중괄호에 인덱스 입력 시 포매팅 순서 지정 가능
print('Hello, %s!! %s' %(name1, name2)) 
print(f'Hello, {name2}!! {name1}??') #가장 최신 포매팅 / js에서 백틱으로 포매팅한 것과 동일 기능
