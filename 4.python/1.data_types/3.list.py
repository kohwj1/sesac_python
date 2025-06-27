my_list = [1,2,3,4,5]
print(my_list)

print(len(my_list))
print(my_list[0])
print(my_list[1])
# print(my_list[5]) #IndexError 유도
print(my_list[4])
print(my_list[-1]) #대부분의 다른 언어에서는 허용하지 않음

print(my_list[1:3]) #인덱스 1은 포함, 인덱스 3은 미포함됨
print(my_list[0:5]) 
print(my_list[0:2]) 
print(my_list[2:4]) #슬라이싱을 연속으로 할 때 유용한 특성


print(my_list[:2]) #시작 슬라이싱 입력 안하면 기본값(0)
print(my_list[2:]) #끝 슬라이싱 입력 안하면 기본값(해당 iter의 길이)

print('-'*10)

my_list.append(6)
print(my_list)
my_list.insert(2,10)
print(my_list)

another_list = [7,8,9]
print(my_list)
print(another_list)
my_list.extend(another_list)
print(my_list)
print(another_list)

my_list.remove(10) #리스트 내의 값이 10인 항목을 삭제 / 같은 게 여러개면? 
print(my_list)

my_list.pop(3) #3번째 인덱스 아이템을 삭제함. 인자 미 입력 시 가장 마지막 아이템 삭제
print(my_list)

my_list.pop() #인자 미 입력 시 가장 마지막 아이템 삭제
print(my_list)

my_list.clear() #리스트 비우기
print(my_list)

print('-'*10)
my_list = [1,2,3,4,5,4,3,2,1]

index_of_3 = my_list.index(3) #아이템 3의 인덱스 위치를 리턴
print(index_of_3)

count_2 = my_list.count(2) #2라는 아이템이 몇 개 있는지
print(count_2)

# my_list.sort() #복제본을 리턴하지 않고 원본을 수정하는 함수 / 옵션 미 입력 시 오름차순 정렬
# print(my_list)

# my_list.sort(reverse=True)
# print(my_list)

sorted_list = sorted(my_list) #원본을 수정하지 않고 복제본을 리턴하는 함수
print(sorted_list)

my_list.reverse() #현재 리스트 순서 뒤집기 (정렬 X)
print(my_list)

my_list2 = my_list.copy()
print(my_list2)

numbers = [x for x in range(10)] #리스트 정의 시 반복문 또는 조건문을 통해 리스트 아이템을 정의
print(numbers)

numbers2 = [x for x in range(1,11) if x % 2 == 0] #리스트 정의 시 반복문 또는 조건문을 통해 리스트 아이템을 정의
print(numbers2)