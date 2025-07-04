from abc import ABC, abstractmethod

class Displayable(ABC):
    registry = {}

    def __init_subclass__(cls, **kwargs):  #나를 상속받은 자녀가 자동으로 실행하게 되는 함수
        super().__init_subclass__(**kwargs)
        Displayable.registry[cls] = cls  #나를 상속해간 자녀 클래스를 딕셔너리에 넣는

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

class OrderItem(Displayable):
    def display(self):
        print('주문상품 객체 처리')

class DisplayData:
    def __init__(self, data):
        handler = Displayable.registry.get(type(data))
        if handler:  #있으면
            data.display()
        else:
            print('미지원 타입')

# DisplayData(User())
# DisplayData(Store())
# DisplayData(Item())
DisplayData(OrderItem()) #제대로 상속받은 경우 정상 동작

