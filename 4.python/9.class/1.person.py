class Person:
    #객체(인스턴스) 생성 시 실행되는 메소드
    def __init__(self, name, age):
        self.name = name #객체의 속성(attribute): 개별 데이터를 저장
        self.age = age

    def __str__(self):
        return f'Person(name={self.name}, age={self.age})'

    def __eq__(self, other): #self와 다른 객체를 비교할 때의 조건?
        return self.name == other.name and self.age == other.age

    #메소드: 객체 안에 있는 함수
    def greet(self):
        print(f'안녕하세요 저는 {self.name}입니다')
    
    def ride_car(self):
        print('자동차를 탑니다')


person1 = Person('김철수',30)
person2 = Person('홍길동',25)
person3 = Person('아무개',22)
person4 = Person('김철수',30)

person1.greet()
person1.ride_car()

person2.greet()
person2.ride_car()

print(person1)
print(person1 == person2)
print(person2 == person3)
print(person3 == person4)
print(person4 == person3)