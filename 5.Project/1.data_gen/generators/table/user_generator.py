from generators.user.name import NameGenerator
from generators.user.gender import GenderGenerator
from generators.common.date import DateGenerator
from generators.common.address import AddressGenerator
from generators.common.uuid import UuidGenerator

class UserGenerator:
    def __init__(self):
        self.id_gen = UuidGenerator()
        self.name_gen = NameGenerator()
        self.bday_gen = DateGenerator()
        self.gender_gen = GenderGenerator()
        self.address_gen = AddressGenerator()
        
    def generate_user(self, count:int) -> list:
        users = []
        for _ in range(count):
            user_id = self.id_gen.generate_uuid()
            name = self.name_gen.generate_name()
            gender = self.gender_gen.generate_gender()
            birthday = self.bday_gen.generate_date('birth')
            age = self.bday_gen.generate_age()
            address = self.address_gen.generate_address()
            users.append((user_id, name, gender, age, birthday, address))
        return users