from generators.user.name import Name
from generators.user.gender import Gender
from generators.common.date import Date
from generators.common.address import Address
from generators.common.uuid import Uuid
from registry import register

@register('user')
class User:
    def __init__(self):
        self.header = ['Id', 'Name', 'Gender', 'Age', 'Birthday', 'Address']
        self.id_gen = Uuid()
        self.name_gen = Name()
        self.bday_gen = Date()
        self.gender_gen = Gender()
        self.address_gen = Address()
        
    def generate(self, count:int) -> list:
        users = []
        for _ in range(count):
            user_id = self.id_gen.generate()
            name = self.name_gen.generate()
            gender = self.gender_gen.generate()
            birthday = self.bday_gen.generate_date('birth')
            age = self.bday_gen.generate_age()
            address = self.address_gen.generate()
            users.append((user_id, name, gender, age, birthday, address))
        return users, self.header