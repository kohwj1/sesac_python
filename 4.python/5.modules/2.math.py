# https://docs.python.org/ko/3.10/library/math.html (기본 수학 연산을 위한 모듈)

import math

print(math.pi)

#원의 넓이 = 반지름 ^ 2 * pi

radius = 5
area = math.pi * radius ** 2
area2 = math.pi * math.pow(radius,2)  #math.pow(x, y) == x ** y

print(f'반지름이 {radius}인 원의 넓이는 {area2:10.2f}입니다')  #:5.2f == 정수는 앞에 공백을 채워 최소 10자리 표시, 소숫점 2번째 자리까지 표시

my_text = 'hi'
print(f'[{my_text:>10}]')
print(f'[{my_text:<10}]')
print(f'[{my_text:^10}]')