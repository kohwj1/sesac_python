x = 5
y = 3
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y) # 5를 3으로 나눈 나머지 (=2)
print(x**y) #5의 3승

str_x = '100'
# print(x + str_x)
# 자료형이 일치하지 않아 line 11에서 오류 발생함 (typeerror)

int_x = int(str_x) # 정수로 변환 (기본값: 10진수, 다른 숫자를 아규먼트로 넘기면 해당 진수로 변환 가능)

print('문자열 x:', str_x)
print('정수 x:', int_x)

print(x + int_x)

# & 연산자
print(1 & 1)
print(1 & 0)
print(0 & 1)
print(0 & 0)

# | 연산자
print(1 | 1)
print(1 | 0)
print(0 | 1)
print(0 | 0)


print(x & y) # 1
print(x | y)  # 7