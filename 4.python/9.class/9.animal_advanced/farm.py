from animal import Animal
from typing import List

class Farm:
    def __init__(self, name):
        self.farm_list: List[Animal] = []
        self.name = name

    def add_animal(self, animal:Animal):
        self.farm_list.append(animal)

    def feed_all(self) -> None:
        for animal in self.farm_list:
            animal.feed('사과')
    
    def play_all(self) -> None:
        for animal in self.farm_list:
            animal.energy -= 10
    
    def show_all(self):
        for animal in self.farm_list:
            print(f'{animal.name} / {animal.sound} / {animal.energy}')

    def move_all(self):
        print(f'동물들 움직이는중')
        for animal in self.farm_list:
            animal.move()

    def speak_all(self):
        print(f'동물을 말시키는중')
        for animal in self.farm_list:
            animal.speak()