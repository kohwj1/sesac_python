class Animal:
    def __init__(self, name:str) -> None:
        self.__name:str = name
        self.energy = 100

    @property
    def name(self):
        return self.__name