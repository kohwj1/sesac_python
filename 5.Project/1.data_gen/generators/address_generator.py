import random

class AddressGenerator:
    def __init__(self, city_path):
        self.cities = self.load_data_from_file(city_path)

    def load_data_from_file(self, file_path):
        with open(file_path,'r',encoding='UTF-8') as file:
            data = file.read().splitlines() #한줄당 이름 하나씩 들어있는 경우
        return data

    def city(self):
        return random.choice(self.cities)

    def generate_address(self):
        city = self.city()
        street_num = random.randint(1,100)
        post_num = random.randint(1,100)
        return f'{city}구 {street_num}길 {post_num}'
    
# if __name__ == '__main__':
#     my_address = AddressGenerator('cities.txt')
#     print(my_address.generate_address())