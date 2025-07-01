from generators.name_generator import NameGenerator
from generators.birthdate_generator import BirthGenerator
from generators.gender_generator import GenderGenerator
from generators.address_generator import AddressGenerator
from generators.uuid_generator import UuidGenerator

class UserGenerator:
    def __init__(self):
        self.id_gen = UuidGenerator()
        self.name_gen = NameGenerator('names.txt')
        self.bday_gen = BirthGenerator()
        self.gender_gen = GenderGenerator()
        self.address_gen = AddressGenerator('cities.txt')
        
    def generate_user(self, count):
        users = []
        for _ in range(count):
            user_id = self.id_gen.generate_uuid()
            name = self.name_gen.generate_name()
            gender = self.gender_gen.generate_gender()
            age = self.bday_gen.generate_age()
            birthday = self.bday_gen.generate_birth()
            address = self.address_gen.generate_address()
            users.append((user_id, name, gender, age, birthday, address))
        return users