from generators.user_generator import UserGenerator
from generators.store_generator import StoreGenerator
from generators.item_generator import ItemGenerator
import sys

class UserDisplayData(UserGenerator):
    def print_data(self, count):
        data = self.generate_user(count)
        for user_id, name, birth, gender, address in data:
            print(f'ID:{user_id}', end=',')
            print(f'Name:{name}', end=',')
            print(f'Birthday:{birth}', end=',')
            print(f'Gender:{gender}', end=',')
            print(f'Address:{address}')

class StoreDisplayData(StoreGenerator):
    def print_data(self, count):
        data = self.generate_store(count)
        for store_id, store_name, store_type, store_address in data:
            print(f'ID:{store_id}', end=',')
            print(f'Name:{store_name}', end=',')
            print(f'Type:{store_type}', end=',')
            print(f'Address:{store_address}')

class ItemDisplayData(ItemGenerator):
    def print_data(self):
        data = self.generate_item()
        for store_id, store_name, store_type, store_address in data:
            print(f'ID:{store_id}', end=',')
            print(f'Name:{store_name}', end=',')
            print(f'Type:{store_type}', end=',')
            print(f'Address:{store_address}')
            
#최종 실행
# user_data = UserDisplayData()
# user_data.print_data(10)
# store_data = StoreDisplayData()
# store_data.print_data(10)
item_data = ItemDisplayData('item.json')
item_data.print_data()