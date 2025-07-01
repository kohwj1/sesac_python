
from generators.uuid_generator import UuidGenerator
import json

class ItemGenerator:
    def __init__(self, file_path):
        self.id_gen = UuidGenerator()
        self.item_menu = json.loads(file_path)
        
    def generate_item(self):
        items = []
        for drink_type in range(self.item_menu):
            for drink, price in drink_type.items():
                item_id = self.id_gen.generate_uuid()
                item_name = drink
                item_type = drink_type
                item_price = price
                items.append((item_id, item_name, item_type, item_price))
        return items
    

if __name__ == '__main__':
    my_item = ItemGenerator('item.json')
    print(my_item.generate_item())