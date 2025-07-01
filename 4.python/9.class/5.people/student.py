from person import Person

class Student(Person): #Person 클래스 내용을 상속함
    def __init__(self,name,age,student_id):
        super().__init__(name,age)  #부모 클래스 (super)를 통해 초기 세팅
        self.__student_id = student_id

    def study(self):
        print(f'{self.name}은 학교에서 공부하고 있습니다. 학번: {self.__student_id}')