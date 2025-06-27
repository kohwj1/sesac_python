my_dict = {'name':'Alice', 'age':25,'location':'Seoul'}
print(my_dict)
print(my_dict['name'])

user1 = {'name':'Bob', 'age':30,'location':'Busan'}
print(user1['name'])
print(user1['age'])
print(user1['location'])

user1['age'] = 31
print(user1)

user1['car'] = '현대 K5'
print(user1)

user1['car'] = ''  #car 키에 빈 value를 할당함 (키가 삭제된 것이 아님)
print(user1)

#예약어는 변수명으로 쓸 수 없다. 함수명에 쓸 경우 기존 내장함수가 동작하지 않음.(사실상 사용 불가) 주요 키워드는 외워야
del user1['car'] #car 키를 삭제
print(user1)

#json / dict 따옴표 차이

print(user1.keys())
print(user1.values())
print(user1.items()) #key-value가 튜플로 묶인 개체 전달됨 --> 리스트처럼 쓰려면 캐스팅해줘야

useritem_list = list(user1.items())
print(useritem_list[0])
# useritem_list[0][1] = 'Peter' #내부 아이템은 튜플이므로 수정 불가