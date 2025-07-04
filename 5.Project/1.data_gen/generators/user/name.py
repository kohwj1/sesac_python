from generators.common.getData import GetData

class Name(GetData):
    def generate(self) -> str:
        last_name = self.get_rand('data/family_names.txt')
        first_name = self.get_rand('data/names.txt')
        return f'{last_name}{first_name}'