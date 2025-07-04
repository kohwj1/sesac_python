from generators.table.user import User
from generators.table.store import Store
from generators.table.item import Item
from generators.table.order import Order
from generators.table.orderItem import OrderItem

class TableType():
    instance = {'user':(['Id','Name','Gender','Age','Birthdate','Address'], User()),
                'store':(['Id','Name','Type','Address'], Store()),
                'item':(['Id','Name','Type','UnitPrice'], Item()),
                'order':(['Id','OrderAt','StoreId','UserId'], Order()),
                'orderitem': ([['Id','OrderId','ItemId']], OrderItem())
                }
    @classmethod    
    def add_type(cls,key:str,value:tuple):
        cls.instance[key] = value