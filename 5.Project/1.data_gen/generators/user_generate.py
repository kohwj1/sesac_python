from generators.name_generator import NameGenerator
from generators.birthdate_generator import BirthGenerator
from generators.gender_generator import GenderGenerator
from generators.address_generator import AddressGenerator
from generators.userid_generator import UserIdGenerator

class UserGenerator:
    def __init__(self):
        self.id_gen = UserIdGenerator()
        self.name_gen = NameGenerator('names.txt')
        self.bday_gen = BirthGenerator()
        self.gender_gen = GenderGenerator()
        self.address_gen = AddressGenerator('cities.txt')
        
    def generate_user(self, count):
        users = []
        for _ in range(count):
            user_id = self.id_gen.generate_userid()
            name = self.name_gen.generate_name()
            bday = self.bday_gen.generate_birth()
            gender = self.gender_gen.generate_gender()
            address = self.address_gen.generate_address()
            users.append((user_id, name, bday, gender, address))
        return users