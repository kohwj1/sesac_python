#251
#클래스: 객체를 설정하기 위한 구조, 설계도
#객체: 클래스를 통해 생성된 인스턴스?

#252
class Human:
    pass

#253
areum = Human()

#254
class Human:
    def __init__(self):
        print('응애응애')
areum = Human()

#255
class Human:
    def __init__(self, name, age, gender):
        print('응애응애2')
        self.name = name
        self.age = age
        self.gender = gender
areum = Human("아름", 25, "여자")

#256
print(areum.name)
print(areum.age)
print(areum.gender)

#257
class Human:
    def __init__(self, name, age, gender):
        print('응애응애3')
        self.name = name
        self.age = age
        self.gender = gender
    def who(self):
        print(f'이름: {self.name}, 나이: {self.age}, 성별: {self.gender}')

areum = Human("조아름", 25, "여자")
areum.who()

#258
class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def setInfo(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

#259
class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def __del__(self):
        print('나의 죽음을 알리지 말라')

areum = Human('?', 0, '?')
del areum


#260
# OMG 클래스의 print 함수 호출 시 객체 자신이 매개변수로 전달되었으나, 클래스 함수에서 인자를 받지 않게 되어 있어 불필요한 argument 오류가 발생함.
# 오류를 수정하려면 def print(self) 형태로 수정되어야 함