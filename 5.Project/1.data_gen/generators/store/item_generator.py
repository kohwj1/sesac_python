
from generators.common.uuid_generator import UuidGenerator
import json

class ItemGenerator:
    def __init__(self, file_path):
        self.id_gen = UuidGenerator()
        self.item_menu = self.item_parse(file_path)
    
    def item_parse(self, file_path) -> dict:
        with open(file_path, 'r', encoding='UTF-8') as file:
            data_str = file.read()
        data = json.loads(data_str)
        return data
        
    def generate_item(self):
        items = []
        for drink_type in self.item_menu:
            for drink, price in self.item_menu[drink_type].items():
                item_id = self.id_gen.generate_uuid()
                item_type = drink_type
                item_name = f'{drink} {item_type}'
                item_price = price
                items.append((item_id, item_name, item_type, item_price))
        return items