from cat import Cat
from dog import Dog
from farm import Farm
from panda import Panda

if __name__ == '__main__':
    myFarm1 = Farm('sesac')

    buddy = Dog('buddy')
    kitty = Cat('kitty')
    fubao = Panda('Fubao')

    myFarm1.add_animal(buddy)
    myFarm1.add_animal(kitty)
    myFarm1.add_animal(fubao)

    for _ in range(10):
        buddy.move()
        kitty.move()

    myFarm1.move_all()
    myFarm1.speak_all()
    myFarm1.move_all()
    myFarm1.speak_all()