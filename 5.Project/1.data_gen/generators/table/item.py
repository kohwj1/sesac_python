from generators.common.uuid import Uuid
from generators.store.price import Price
from generators.store.itemname import ItemName

class Item:
    def __init__(self):
        self.item_menu = ItemName()
        self.id_gen = Uuid()
        self.price = Price()
        
    def generate(self, count:int) -> list:
        items = []
        for _ in range(count):
            item_id = self.id_gen.generate()
            item_name = self.item_menu.generate()
            item_type = item_name.split()[1]
            item_price = self.price.generate()
            items.append((item_id, item_name, item_type, item_price))
        return items
    
if __name__ == '__main__':
    test_instance = Item()
    print(test_instance.generate_item(40))