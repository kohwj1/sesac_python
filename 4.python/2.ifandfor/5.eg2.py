users = [
    {'name':'Alice', 'age':25, 'location':'Seoul','car':'BMW'},
    {'name':'Bob', 'age':30, 'location':'Busan','car':'Mercedes'},
    {'name':'Chalie', 'age':35, 'location':'Daegu','car':'Audi'},
    {'name':'Chalie', 'age':40, 'location':'Suwon','car':'Audi'},
    {'name':'Bob', 'age':40, 'location':'Jeju','car':'Mercedes'}
]

# for u in users:
#     print(u)

def find_user(name):
    for u in users:
        if u['name'] == name:
            return u

# print(find_user('Alice'))
# print(find_user('Bob'))
# print(find_user('David')) #없으므로 None이 출력됨

def find_users(name):
    result = []
    for u in users:
        if u['name'] == name:
            result.append(u)
    return result

# print(find_users('Bob'))
# print(find_users('bob'))  --> 대소문자가 일치하지 않아 if 조건에 걸리지 않음

def find_users_caseinsensitive(name):
    result = []
    for u in users:
        if u['name'].lower() == name.lower(): #대소문자 구분을 없애기 위해 강제 소문자화
            result.append(u)
    return result

# print(find_users_caseinsensitive('Bob'))
# print(find_users_caseinsensitive('bob'))
# print(find_users_caseinsensitive('BOB'))

def find_user2(name ,age):
    for u in users:
        # and를 &로 사용할 경우, 괄호로 묶어 연산자 처리 우선순위로 인한 오동작이 발생하지 않게 해야 함
        # if u['name'] == name & u['age'] == age: --> name과 u['age']의 and연산이 먼저 되면서 오류 발생
        # if (u['name'] == name) & (u['age'] == age): --> 정상 동작
        if u['name'] == name and u['age'] == age: #가장 파이썬스러움 (자연어에 가까운)
            return u

# print(find_user2('Alice',25))
# print(find_user2('Bob',40))

def find_user3(name=None ,age=None):
    result = []
    for u in users:
        if name:
            if u['name'] == name: #가장 파이썬스러움 (자연어에 가까운)
                if age:
                    if u['age'] == age:
                        result.append(u) #이름, 나이 모두 일치할 경우
                else:
                    result.append(u) #이름 일치, 나이 정보 없을 경우
        elif age:
            if u['age'] == age:
                result.append(u) #나이 일치, 이름 모를 경우
        else:
            result.append(u)
    
    return result

# print(find_user3(name='Bob'))
# print(find_user3(age=40))
print(find_user3(name='Bob',age=40))
