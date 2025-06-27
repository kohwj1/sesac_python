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
    temp_list = [a,b,c]
    temp_list.sort()
    print(temp_list[-1])

#221
def print_reverse(word):
    print(''.join(reversed(word)))

#222
def print_score(score_list):
    print(sum(score_list)/len(score_list))

#223
def print_even(num_list):
    for num in num_list:
        if num % 2 == 0:
            print(num)

#224
def print_keys(your_dict):
    for key in list(your_dict.keys()):
        print(key)

#225
def print_value_by_key(your_dict, key):
    print(your_dict[key])

#226
def print_5xn(word):
    repeat_count = len(word)//5
    for i in range(repeat_count):
        print(word[5*i:5*(i+1)])
    
    if len(word) % 5 > 0:
        print(word[5*repeat_count:])

#227
def print_mxn(word, count):
    repeat_count = len(word)//count
    for i in range(repeat_count):
        print(word[count*i:count*(i+1)])
    
    if len(word) % count > 0:
        print(word[count*repeat_count:])

#228
def calc_monthly_salary(annual_salary):
    print(int(annual_salary/12))

#229
#"왼쪽: 100"
#"오른쪽: 200"

#230
#"왼쪽: 200"
#"오른쪽: 100"

#231
#4

#232
def make_url(site):
    return f'www.{site}.com'

#233
def make_list(word):
    return [char for char in word]

#234
def pickup_even(your_list):
    return [i for i in your_list if i % 2 == 0]

#235
def convert_int(string_int):
    temp_int = string_int.replace(',','')
    return int(temp_int)

#236
#22
#a = 함수(10) --> 14
#b = 함수(a) --> 14+4 = 18
#c = 함수(b) --> 18+4 = 22

#237
# 22
# 괄호 안쪽부터 연산하면서 함수를 총 3번 거치게 되므로 10 + 4 + 4 + 4 = 22가 됨

#238
# 140 = (10+4) * 10

#239
# 16
# c = 함수2(10) --> return 함수1(12) = 12+4 = 16 

#240
#28
#1. 함수2(2) = 함수1(12)
#2. 함수1(12) = 함수0(14)
#3. 함수0(14) = 14 * 2 = 28