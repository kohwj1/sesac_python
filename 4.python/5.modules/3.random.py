# https://docs.python.org/ko/3.10/library/random.html

import random
# print(random.random()) #0 이상 1 미만의 임의의 수 리턴
# print(random.randinit(1, 100)) #1 이상 100 '이하'의 임의의 수 리턴


def roll_dice(count):
    print(f'-----주사위 {count} 번 시행 결과-----')
    
    result = {k:0 for k in range(1,7)} #딕셔너리도 컴프리헨션 가능!

    for i in range(count):
        result[random.randint(1,6)] += 1

    for dice_num, dice_count in result.items():
        print(f'{dice_num}이 나온 횟수: {dice_count}번, 확률: {dice_count / count:.2%}')

#주사위 백번/천번/만번 던져서 각 숫자가 나올 확률 출력
roll_dice(100_000)