class Car:
    def __init__(self, make, model):
        self.__make = make
        self.__model = model
        self.__odometer = 0 #주행거리
    
    def get_name(self):
        long_name = f'{self.__make} {self.__model}'
        return long_name.title() #띄어쓰기 단위로 첫 글자를 대문자화
    
    def read_odometer(self):
        print(f'이 차의 주행거리는 현재 {self.__odometer}km입니다.')
    
    def update_odometer(self,mileage):
        if self.__odometer < mileage:
            self.__odometer = mileage
        else:
            print('주행거리를 속일 수 없습니다.')

    def increment_odometer(self, distance):
        self.__odometer += distance