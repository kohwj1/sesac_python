for i in range(5): # for i in [0,1,2,3,4] 와 동일한 내용
    print(i)

for i in range(1,10):
    print(i)

for i in range(1,10,2): #2씩 건너뛴다 (미입력 시 1씩)
    print(i)

for i in range(1,10,3): #3씩 건너뛴다
    print(i)

basket = ['apple', 'banana', 'cherry']
for fruit in basket:
    print(fruit)

for index, fruit in enumerate(basket):  #enumerate 없이 시도하면 언패킹 오류 발생
    print(index, fruit)


str = 'Hello, World!'

for char in str: #string은 반복 순회(iterate) 가능
    print(char)

count_o = 0
for char in str:
    if char == 'o':
        count_o += 1

print(f'{str} 문장 내의 o의 갯수는 {count_o}입니다.')

count_l = 0
for char in str:
    if char == 'l':
        count_l += 1

print(f'{str} 문장 내의 l의 갯수는 {count_l}입니다.')