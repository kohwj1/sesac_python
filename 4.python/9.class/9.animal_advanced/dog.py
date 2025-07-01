from animal import Animal

class Dog(Animal):
    def __init__(self, name:str):
        super().__init__(name)
        self.move_energy = 10
        self.sound = 'Woof'
    
    def move(self) -> None:
        if self.energy < self.move_energy:
            print('움직일 수 없어요!')
        else:
            self.energy -= self.move_energy
            print(f'{self.name}의 남은 에너지: {self.energy}')

    @property
    def speak_sound(self) -> str:
        return self.__speak_sound