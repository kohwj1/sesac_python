numbers = [1,2,3,4,5,6,7,8,9,10]

for num in numbers:
    if num % 2 == 0:
        print(f'숫자 {num}은 짝수입니다.')
    else:
        print(f'숫자 {num}은 홀수입니다.')


def getEvenNumbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            # print(f'숫자 {num}은 짝수입니다.')
            even_numbers.append(num)
    return even_numbers

even = getEvenNumbers(numbers)
print(f'짝수는: {even}')


def getGrade(score):
    if score >= 90:
        return 'A'
    elif score >= 80: #return으로 윗줄에서 함수 리턴을 받으며 끝나기 때문에 elif가 아니어도 동작함
        return 'B'
    elif score >= 70:
        return 'C'
    else:
        return 'F'
    
students = {
    '김민준': 78,
    '이서윤': 72,
    '박지훈': 93,
    '최유진': 86,
    '정하늘': 64,
    '강민서': 86,
    '윤지호': 96,
    '오예린': 85,
    '한도윤': 75,
    '홍서아': 99
}
a_student = []
student_name = list(students.keys())

for name in student_name:
    if getGrade(students[name]) == 'A':
        a_student.append(name)

print(f'A 성적 학생: {a_student}')

a_student_another = [name for name in student_name if getGrade(students[name]) == 'A']
print(f'A 성적 학생: {a_student_another}')