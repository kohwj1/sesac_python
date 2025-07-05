from generators.table.user import User
from generators.table.store import Store
from generators.table.item import Item
from generators.table.order import Order
from generators.table.orderItem import OrderItem

class TableType():
    instance = {'user':User(), 
                'store':Store(),
                'item':Item(),
                'order':Order(),
                'orderitem':OrderItem()
                }
    @classmethod    
    def add_type(cls,key:str,value:tuple):
        cls.instance[key] = value