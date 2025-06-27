score = 80
if score >= 90:
    print('A학점')
elif score >= 80:
    print('B학점')
elif score >= 70:
    print('C학점')
else:
    print('F학점')


def getGrade(score):
    if score >= 90:
        grade = 'A학점'
    elif score >= 80:
         grade = 'B학점'
    elif score >= 70:
         grade = 'C학점'
    else:
         grade = 'F학점'
    return grade

john = getGrade(70)
jane = getGrade(95)

print('john 학점:',john)
print('jane 학점:',jane)

user = input('점수를 입력하시오:')
user_score = getGrade(int(user))
print('사용자의 점수는:',user_score,"입니다")

