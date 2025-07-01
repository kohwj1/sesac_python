import random

class StoreTypeGenerator:
    def __init__(self, file_path):
        self.store_types = self.load_data_from_file(file_path)

    def load_data_from_file(self, file_path):
        with open(file_path,'r',encoding='UTF-8') as file:
            data = file.read().splitlines() #한줄당 이름 하나씩 들어있는 경우
        return data

    def generate_storetype(self):
        return random.choice(self.store_types)
    
if __name__ == '__main__':
    test_instance = StoreTypeGenerator()
    print(test_instance.generate_storetype())