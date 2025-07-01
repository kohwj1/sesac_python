class Person:
    def __init__(self,name:str,age:int) -> None:
        self.__name:str = name
        self.__age:int = age

    @property
    def name(self) -> str:
        return self.__name
    @property
    def age(self) -> int:
        return self.__age
    
    @name.setter
    def name(self,name:str) -> None:
        self.__name = name
    
    @age.setter
    def age(self,age:int) -> None:
        if age >= 0:
            self.__age = age
        else:
            print('나이는 0보다 크거나 같아야 합니다')

    def greet(self) -> None:
        print(f'나의 이름은 {self.__name}이고 나이는 {self.__age}입니다.')