a = ['철수', '영희', '민수', '지현', '서연']
b = ['영희', '민수', '지수', '서연', '하나']
c = ['철수', '지현', '지수', '서연', '나영']

#문제: a와 b를 모두 좋아하지만 c는 좋아하지 않는 사람?

a_or_b = a[:]
a_or_b.extend(b)
temp_dict = {}

for people in a_or_b:
    temp_dict[people] = 0

answer = [people for people in temp_dict.keys() if people in a and people in b and people not in c]
print(answer)