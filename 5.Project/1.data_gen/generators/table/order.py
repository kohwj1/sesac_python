from generators.common.uuid import Uuid
from generators.common.getData import GetData
from generators.order.orderAt import OrderedAt
import random
from registry import register

@register('order')
class Order:
    def __init__(self):
        self.header = ['Id', 'OrderAt', 'StoreId', 'UserId']
        self.id_gen = Uuid()
        self.order_at = OrderedAt()
        self.store_id = GetData()
        self.user_id = GetData()
        
    def generate(self, count:int) -> list:
        orders = []
        for _ in range(count):
            order_id = self.id_gen.generate()
            order_at = self.order_at.generate()
            store_id = random.choice(self.store_id.get_uuid('store'))
            user_id = random.choice(self.user_id.get_uuid('user'))
            orders.append((order_id, order_at, store_id, user_id))
        return orders, self.header
    
if __name__ == '__main__':
    test_instance = Order()
    print(test_instance.generate(40))