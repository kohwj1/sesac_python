from generators.store.storetype import StoreTypeGenerator
from generators.common.address import AddressGenerator
from generators.common.uuid import UuidGenerator
import random

class StoreGenerator():
    def __init__(self):
        self.id_gen = UuidGenerator()
        self.storetype_gen = StoreTypeGenerator()
        self.address_gen = AddressGenerator()
        
    def generate_store(self, count:int) -> list:
        stores = []
        for _ in range(count):
            store_id = self.id_gen.generate_uuid()
            store_type = self.storetype_gen.generate_storetype()
            store_address = self.address_gen.generate_address()
            store_division = store_address.split()[1][:-1]
            store_name = f'{store_type} {store_division}{random.randint(1,9)}호점'
            stores.append((store_id, store_name, store_type, store_address))
        return stores

if __name__ == '__main__':
    my_store = StoreGenerator()
    print(my_store.generate_store(1))