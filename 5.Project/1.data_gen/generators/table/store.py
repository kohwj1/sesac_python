from generators.store.storetype import StoreType
from generators.common.address import Address
from generators.common.uuid import Uuid
import random
from registry import register

@register('store')
class Store:
    def __init__(self):
        self.header = ['Id', 'StoreName', 'StoreType', 'Address']
        self.id_gen = Uuid()
        self.storetype_gen = StoreType()
        self.address_gen = Address()
        
    def generate(self, count:int) -> list:
        stores = []
        for _ in range(count):
            store_id = self.id_gen.generate()
            store_type = self.storetype_gen.generate()
            store_address = self.address_gen.generate()
            store_division = store_address.split()[1][:-1]
            store_name = f'{store_type} {store_division}{random.randint(1,9)}호점'
            stores.append((store_id, store_name, store_type, store_address))
        return stores, self.header

if __name__ == '__main__':
    my_store = Store()
    print(my_store.generate_store(1))