from generators.common.uuid import UuidGenerator
from generators.common.getData import GetData
import random

class OrderItemGenerator:
    def __init__(self):
        self.id_gen = UuidGenerator()
        self.order_id = GetData()
        self.item_id = GetData()
        
    def generate_orderitem(self, count:int) -> list:
        orderitems = []
        for _ in range(count):
            orderitem_id = self.id_gen.generate_uuid()
            order_id = random.choice(self.order_id.get_uuid('order'))
            item_id = random.choice(self.item_id.get_uuid('item'))
            orderitems.append((orderitem_id, order_id, item_id))
        return orderitems
    
if __name__ == '__main__':
    test_instance = OrderItemGenerator()
    print(test_instance.generate_orderitem(40))