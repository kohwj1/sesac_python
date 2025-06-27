#201
def print_coin():
    print('비트코인')

#202
print_coin()


#203
for i in range(100):
    print_coin()

#204
def print_coins():
    print('비트코인\n'*100)

#205
#Python의 인터프리터 언어 특성상 위에서부터 라인 한줄씩 실행하는데 hello() 함수를 정의하기 전에 먼저 호출했기 때문.

#206
# A
# B
# C
# A
# B

#207
# A
# C
# B

#208
# A
# C
# B
# E
# D

#209
# B
# A

#210
# B
# C
# B
# C
# B
# C
# A

#211
# 안녕
# Hi

#212
# 7
# 15

#213
#함수 인자 '문자열' 누락

#214
#a의 argument가 숫자가 아니어서 연산 과정 도중 TypeError 발생

#215
def print_with_smile(word):
    print(word+':D')

#216
print_with_smile('안녕하세요')

#217
def print_upper_price(price):
    print(price*1.3)

#218
def print_sum(a,b):
    print(a+b)

#219
def print_arithmetic_operation(a,b):
    print(f'{a} + {b} = {a+b}')
    print(f'{a} - {b} = {a-b}')
    print(f'{a} * {b} = {a*b}')
    print(f'{a} / {b} = {a/b}')

#220
def print_max(a,b,c):
    if (a>b and a>c) or (a==b==c) or (a==b and b>c):
        print(a)
    elif (b>a and b>c) or (b==c and b>a):
        print(b)
    elif (c>a and c>b) or (c > a and c==b):
        print(c)

#221
def print_reverse(word):
    print(''.join(reversed(word)))

#222
# def print_score(score_list):