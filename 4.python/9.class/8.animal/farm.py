from animal import Animal
from typing import List
from cat import Cat
from dog import Dog

class Farm:
    def __init__(self, name):
        self.farm_list: List[Animal] = []
        self.name = name

    def add_animal(self, animal:Animal):
        self.farm_list.append(animal)

    def feed(self,food:str):
        self.energy += 50
        print(f'{self.name}은 {food}를 먹었습니다. 잔여 에너지: {self.energy}')

    def feed_all(self) -> None:
        for animal in self.farm_list:
            animal.feed('사과')
    
    def play_all(self) -> None:
        for animal in self.farm_list:
            animal.energy -= 10
    
    def show_all(self):
        for animal in self.farm_list:
            print(f'{animal.name} / {animal.speak_sound} / {animal.energy}')