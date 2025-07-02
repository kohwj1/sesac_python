from generators.common.uuid import UuidGenerator
from generators.common.getData import GetData
from generators.order.orderAt import OrderedAtGenerator
import random

class OrderGenerator:
    def __init__(self):
        self.id_gen = UuidGenerator()
        self.order_at = OrderedAtGenerator()
        self.store_id = GetData()
        self.user_id = GetData()
        
    def generate_order(self, count:int) -> list:
        orders = []
        for _ in range(count):
            order_id = self.id_gen.generate_uuid()
            order_at = self.order_at.generate_orderdate()
            store_id = random.choice(self.store_id.get_uuid('store'))
            user_id = random.choice(self.user_id.get_uuid('user'))
            orders.append((order_id, order_at, store_id, user_id))
        return orders
    
if __name__ == '__main__':
    test_instance = OrderGenerator()
    print(test_instance.generate_order(40))