class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name
    @property
    def age(self):
        return self.__age
    
    @name.setter
    def name(self,name):
        self.__name = name
    
    @age.setter
    def age(self,age):
        if age >= 0:
            self.__age = age
        else:
            print('나이는 0보다 크거나 같아야 합니다')

    def greet(self):
        print(f'나의 이름은 {self.__name}이고 나이는 {self.__age}입니다.')