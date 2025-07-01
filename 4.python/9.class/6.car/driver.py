from person import Person

class Driver(Person):
    def __init__(self, name, age, license_type, car=None): #argument=None이면 optional
        super().__init__(name, age)
        self.__license_type = license_type
        self.__car = car
    
    def assign_car(self,car):
        self.__car = car
        print(f'{self.name}이 {self.__car.get_name()}을 소유하였습니다.')
    
    def drive(self, distance):
        if self.__car:
            print(f'{self.name}은 {self.__car.get_name()}의 운전을 시작합니다.')
            self.__car.increment_odometer(distance)
        else:
            print('소유한 차량이 없습니다.')
