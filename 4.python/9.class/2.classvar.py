class Person:
    #공통 영역
    __count = 0 #앞에 언더바 2개 붙이기: protected / private variable (외부에서 직접 내부변수에 접근 못 하도록 보호됨).
    # 내부 변수에 저장해서 값을 읽어올 때: getter / get_name()
    # 내부 변수에 세팅할 때: setter / set_name()

    #객체(인스턴스) 생성 시 실행되는 메소드
    def __init__(self, name, age):
        self.name = name #객체의 속성(attribute): 개별 데이터를 저장
        self.age = age
        Person.__count += 1 #클래스 변수에 접근해서 1을 증가시킨다 (self.count라고 사용 시 로컬 변수화됨)

    #메소드: 객체 안에 있는 함수
    def greet(self):
        print(f'안녕하세요 저는 {self.name}입니다')
    
    def ride_car(self):
        print('자동차를 탑니다')

    @classmethod #데코레이터: 나의 함수에 기능을 더해줌
    def get_count(cls): #클래스 내부 변수에 접근하므로 인자를 self가 아닌 cls로 받고 데코레이터를 사용
        return cls.__count #

    # @classmethod #데코레이터: 나의 함수에 기능을 더해줌
    # def set_count(cls, count): #클래스 내부 변수에 접근하므로 인자를 self가 아닌 cls로 받고 데코레이터를 사용
    #     cls.__count += 1 #

person1 = Person('김철수',30) #객체 생성 과정 (인스턴시에이션 / 인스턴트화)
print(person1.get_count())
print(person1.__dict__)

person2 = Person('홍길동',25)
print(person1.get_count())

person3 = Person('아무개',29)
print(person1.get_count())