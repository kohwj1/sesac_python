from abc import ABC, abstractmethod

class Animal:
    def __init__(self, name:str) -> None:
        self.__name:str = name
        self.energy = 100

    def feed(self,food:str):
        self.energy += 50
        print(f'{self.name}은 {food}를 먹었습니다. 잔여 에너지: {self.energy}')

    @property
    def name(self):
        return self.__name
    
    def speak(self) -> None:
        print(f'{self.name}은 {self.speak_style()}라고 합니다.')

    def speak_style(self):
        if self.energy >= 80:
            return self.sound.upper()
        elif self.energy >= 50:
            return self.sound.capitalize()
        elif self.energy >= 20:
            return self.sound.lower()
        else:
            return '...'

    @abstractmethod  #이 클래스를 상속하는 하위 클래스들이 반드시 구현해야 한다는 것을 명시
    def move(self) -> None:
        pass