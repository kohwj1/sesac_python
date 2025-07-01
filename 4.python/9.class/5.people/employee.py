from person import Person

class Employee(Person): #Person 클래스 내용을 상속함
    def __init__(self,name,age,company):
        super().__init__(name,age)  #부모 클래스 (super)를 통해 초기 세팅
        self.__company = company

    def greet(self):  #메소드 오버라이딩 (부모 클래스의 메소드를 덮어씀)
        print(f'저는 {self.__company}에서 일하는 {self.name}입니다.') #부모 속성을 getter로 불러옴
    
    def work(self):
        print(f'직원 {self.name}은/는 {self.__company}에서 일하는 중입니다.')