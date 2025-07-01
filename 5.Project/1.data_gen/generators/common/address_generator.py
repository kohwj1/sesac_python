import random

class AddressGenerator:
    def __init__(self, city_path):
        self.division = self.load_data_from_file(city_path)

    def load_data_from_file(self, file_path):
        with open(file_path,'r',encoding='UTF-8') as file:
            data = file.read().splitlines() #한줄당 이름 하나씩 들어있는 경우
        return data

    def city(self):
        megacity = random.choice(['서울', '대전', '대구', '인천', '부산', '울산', '광주', '세종'])
        division = random.choice(self.division)
        return f'{megacity} {division}'

    def generate_address(self):
        city = self.city()
        street_num = random.randint(1,20)
        post_num = random.randint(1,100)
        return f'{city}구 {street_num}길 {post_num}'