from person import Person
from typing import Optional
from car import Car

class Driver(Person):
    def __init__(self, name:str, age:int, license_type:str, car:Optional[Car]=None) -> None: #argument=None이면 optional
        super().__init__(name, age)
        self.__license_type:str = license_type
        self.__car:Optional[Car] = car #타입으로 Car 또는 None이 들어오는 것을 명시
    
    def assign_car(self,car:Car) -> None:
        self.__car = car
        print(f'{self.name}이 {self.__car.get_name()}을 소유하였습니다.')
    
    def drive(self, distance) -> None:
        if self.__car:
            print(f'{self.name}은 {self.__car.get_name()}의 운전을 시작합니다.')
            self.__car.increment_odometer(distance)
            self.__car.read_odometer()
        else:
            print('소유한 차량이 없습니다.')
