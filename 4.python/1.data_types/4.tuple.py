#튜플은 리스트의 특징과 비슷하나, 값을 수정할 수 없는 자료형
my_tuple = (1,2,3,4,5)
print(my_tuple)
print(my_tuple[-1])

# my_tuple[2] = 5 # 타입에러 발생 (아이템 할당 불가)

my_list = list(my_tuple) #리스트 자료형으로 캐스팅
my_list[2] = 5
print(my_list)

my_tuple2 = tuple(my_list)

#튜플 안의 데이터를 여러 개의 변수로 나눠 담을 수 있음 (튜플 언패킹)
a, _, b = (1, 2, 3) #받아오지만 안 쓸 경우 언더바로 버리기 가능
print(a)
print(b)