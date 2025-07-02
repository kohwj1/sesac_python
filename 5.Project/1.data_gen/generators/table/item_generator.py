from generators.common.uuid import UuidGenerator
from generators.store.price import PriceGenerator
from generators.store.itemname import ItemNameGenerator

class ItemGenerator:
    def __init__(self):
        self.item_menu = ItemNameGenerator()
        self.id_gen = UuidGenerator()
        self.price = PriceGenerator()
        
    def generate_item(self, count:int) -> list:
        items = []
        for _ in range(count):
            item_id = self.id_gen.generate_uuid()
            item_name = self.item_menu.generate_itemname()
            item_type = item_name.split()[1]
            item_price = self.price.generate_price()
            items.append((item_id, item_name, item_type, item_price))
        return items
    
if __name__ == '__main__':
    test_instance = ItemGenerator()
    print(test_instance.generate_item(40))