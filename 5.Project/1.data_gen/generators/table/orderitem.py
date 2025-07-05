from generators.common.uuid import Uuid
from generators.common.getData import GetData
import random

class OrderItem:
    def __init__(self):
        self.header = ['Id','OrderId','ItemId']
        self.id_gen = Uuid()
        self.order_id = GetData()
        self.item_id = GetData()
        
    def generate(self, count:int) -> list:
        orderitems = []
        for _ in range(count):
            orderitem_id = self.id_gen.generate()
            order_id = random.choice(self.order_id.get_uuid('order'))
            item_id = random.choice(self.item_id.get_uuid('item'))
            orderitems.append((orderitem_id, order_id, item_id))
        return orderitems, self.header
    
if __name__ == '__main__':
    test_instance = OrderItem()
    print(test_instance.generate(40))