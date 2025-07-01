import random

class AddressGenerator:
    def __init__(self, city_path):
        self.cities = self.load_data_from_file(city_path)

    def load_data_from_file(self, file_path):
        with open(file_path,'r',encoding='UTF-8') as file:
            data = file.read().splitlines() #한줄당 이름 하나씩 들어있는 경우
        return data

    def generate_address(self):
        city = random.choice(self.cities)
        street_num = random.randint(1,100)
        post_num = random.randint(1,100)
        return f'{city} {street_num}길 {post_num}'