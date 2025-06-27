str = 'hello, World!'
str2 = '    welcome to sesac class '
print(str)


print(str.lower())
print(str.upper())
print(str.capitalize()) #문장 단위로 캐피탈라이징 처리
print(str.title()) #띄어쓰기 단위로 캐피탈라이징 처리
print(str2.strip()) #문자열 앞뒤 트림 처리
print(str2.lstrip()) #문자열 좌측 공백 제거처리
print(str2.rstrip()) #문자열 우측 공백 제거처리

words = str2.split()
print(words)
print(words[2].upper())

print(','.join(words))
print(' '.join(words))
print('-'.join(words))

print(str.startswith('Hello'))
print(str.startswith('hello'))