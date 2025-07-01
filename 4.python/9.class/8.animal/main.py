from cat import Cat
from dog import Dog
from farm import Farm

if __name__ == '__main__':
    myFarm1 = Farm('sesac')

    buddy = Dog('buddy')
    kitty = Cat('kitty')

    myFarm1.add_animal(buddy)
    myFarm1.add_animal(kitty)

    myFarm1.feed_all()
    myFarm1.show_all()

    for _ in range(10):
        buddy.move()

    myFarm1.play_all()
    myFarm1.show_all()

    myFarm2 = Farm('house')