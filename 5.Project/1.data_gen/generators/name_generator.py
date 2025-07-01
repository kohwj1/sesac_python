import random

class NameGenerator:
    def __init__(self, file_path):
        # self.names = ['John', 'Jane', 'Michael', 'Emily', 'William', 'Olivia']
        self.names = self.load_data_from_file(file_path)
    
    def load_data_from_file(self, file_path):
        with open(file_path,'r',encoding='UTF-8') as file:
            data = file.read().splitlines() #한줄당 이름 하나씩 들어있는 경우
        return data

    def generate_name(self):
        return random.choice(self.names)