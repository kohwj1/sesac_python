class Car:
    def __init__(self, make:str, model:str) -> None:  #리턴값이 없음
        self.__make:str = make
        self.__model:str = model
        self.__odometer:int = 0 #주행거리
    
    def get_name(self) -> str: #str을 리턴함
        long_name = f'{self.__make} {self.__model}'
        return long_name.title() #띄어쓰기 단위로 첫 글자를 대문자화
    
    def read_odometer(self) -> None:
        print(f'이 차의 주행거리는 현재 {self.__odometer}km입니다.')
    
    def update_odometer(self,mileage:int) -> None:
        if self.__odometer < mileage:
            self.__odometer = mileage
        else:
            print('주행거리를 속일 수 없습니다.')

    def increment_odometer(self, distance:int) -> None:
        self.__odometer += distance