import random

class NameGenerator:
    # def __init__(self):
        # self.names = ['John', 'Jane', 'Michael', 'Emily', 'William', 'Olivia']
        # 기존 하드코딩 되어 있던걸, 파일을 통해서 읽는 방식으로 변경해보기
    def __init__(self, file_path):
        self.names = self.load_data_from_file(file_path)

    def load_data_from_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read().splitlines() # 한줄에 이름이 하나가 있는 경우
        return data

    def generate_name(self):
        return random.choice(self.names)
    
class BirthdateGenerator:
    def generate_birthdate(self):
        year = random.randint(1990, 2010)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        return f"{year}-{month:02d}-{day:02d}"

class GenderGenerator:
    def generate_gender(self):
        return random.choice(['Male', 'Female'])
    
class AddressGenerator:
    # def __init__(self):
        # self.cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
        
    def __init__(self, file_path):
        self.cities = self.load_data_from_file(file_path)

    def load_data_from_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read().splitlines() # 한줄에 이름이 하나가 있는 경우
        return data
        
    def generate_address(self):
        city = random.choice(self.cities)
        street_num = random.randint(1, 100)
        return f"{street_num} {city}"

class UserGenerator:
    def __init__(self):
        self.name_gen = NameGenerator('names.txt')
        self.bday_gen = BirthdateGenerator()
        self.gender_gen = GenderGenerator()
        self.address_gen = AddressGenerator('cities.txt')
        
    def generate_user(self, count):
        users = []
        for _ in range(count):
            name = self.name_gen.generate_name()
            bday = self.bday_gen.generate_birthdate()
            gender = self.gender_gen.generate_gender()
            address = self.address_gen.generate_address()
            users.append((name, bday, gender, address))
        return users

class DisplayData(UserGenerator):
    def print_data(self, count):
        data = self.generate_user(count)
        for name, birthdate, gender, address in data:
            print(f"Name: {name}\nBirthdate: {birthdate}\nGender: {gender}\nAddress: {address}\n")

# 최종 실행
my_data = DisplayData()
my_data.print_data(100)