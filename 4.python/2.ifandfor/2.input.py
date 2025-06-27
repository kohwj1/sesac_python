
def getGrade(score):
    score_int = int(score)
    if score_int >= 90:
        grade = 'A학점'
    elif score_int >= 80:
         grade = 'B학점'
    elif score_int >= 70:
         grade = 'C학점'
    else:
         grade = 'F학점'
    return grade

name = input('이름을 입력하세요:')
score = input('점수를 입력하세요:')
grade = getGrade(score)

print(f'학생 {name}의 성적은 {grade}입니다.')