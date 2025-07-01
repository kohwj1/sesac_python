from animal import Animal

class Dog(Animal):
    def __init__(self, name:str):
        super().__init__(name)
        self.__mov_distance = 10
        self.__speak_sound = 'Woof'

    def speak(self) -> None:
        print(self.__speak_sound)
    
    def move(self) -> None:
        if self.energy < self.__mov_distance:
            print('움직일 수 없어요!')
        else:
            self.energy -= self.__mov_distance
            print(f'{self.name}의 남은 에너지: {self.energy}')

    @property
    def speak_sound(self) -> str:
        return self.__speak_sound