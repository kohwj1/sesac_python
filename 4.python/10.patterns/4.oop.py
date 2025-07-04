from abc import ABC, abstractmethod

class Displayable(ABC):
    @abstractmethod
    def display(self):
        pass

class User(Displayable):
    def display(self):
        print('유저(Displayable) 객체 처리')
class Store(Displayable):
    def display(self):
        print('상점 객체 처리')

class Item(Displayable):
    def display(self):
        print('아이템 객체 처리')

class Order(Displayable):
    def display_test(self):
        print('주문 객체 처리')

class DisplayData:
    def __init__(self, data):
        data.display()

DisplayData(User())
DisplayData(Store())
DisplayData(Item())
DisplayData(Order()) #추상화를 통해 강제된 함수가 구현되어 있지 않아 TypeError 오류 발생: TypeError: Can't instantiate abstract class Order with abstract method display

