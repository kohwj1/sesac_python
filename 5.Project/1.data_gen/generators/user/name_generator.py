from generators.common.get_data import GetData
import random

class NameGenerator(GetData):
    def generate_name(self) -> str:
        last_name = self.get_rand('static/family_names.txt')
        first_name = self.get_rand('static/names.txt')
        return f'{last_name}{first_name}'