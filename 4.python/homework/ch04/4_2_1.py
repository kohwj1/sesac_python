a = ['철수', '영희', '민수', '지현', '서연']
b = ['영희', '민수', '지수', '서연', '하나']
c = ['철수', '지현', '지수', '서연', '나영']

#문제: a와 b를 모두 좋아하지만 c는 좋아하지 않는 사람?

a.extend(b)
a_and_b = list(set(a))
print(a_and_b)

answer = [people for people in a_and_b if people not in c]
print(answer)