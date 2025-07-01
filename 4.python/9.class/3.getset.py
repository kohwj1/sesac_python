class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    @property # 이 메소드는 getter임을 알려주는 데코레이터
    def name(self): #일반적으로 attribute와 맞추는 게 관례..
        return self.__name
    
    @name.setter #속성 'name'에 대한 setter임을 알려주는 데코레이터
    def name(self, name):
        self.__name = name

    @property # 이 메소드는 getter임을 알려주는 데코레이터
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print('나이는 0보다 크거나 같아야 합니다')

    #메소드: 객체 안에 있는 함수
    def greet(self):
        print(f'안녕하세요 저는 {self.__name}입니다')
    
    def ride_car(self):
        print('자동차를 탑니다')

person1 = Person('김철수',30) #객체 생성 과정 (인스턴시에이션 / 인스턴트화)
person2 = Person('홍길동',25)
person3 = Person('아무개',29)

person1.name = '박철수'
person1.age = 31
print(person1.__dict__)