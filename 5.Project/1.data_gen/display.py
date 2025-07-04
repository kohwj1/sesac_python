from generators.table.user_generator import UserGenerator
from generators.table.store_generator import StoreGenerator
from generators.table.item_generator import ItemGenerator
from generators.table.order_generator import OrderGenerator
from generators.table.orderitem_generator import OrderItemGenerator
import csv

class DisplayData(UserGenerator, StoreGenerator, ItemGenerator, OrderGenerator, OrderItemGenerator):
    user_header = ['Id','Name','Gender','Age','Birthdate','Address']
    store_header = ['Id','Name','Type','Address']
    item_header = ['Id','Name','Type','UnitPrice']
    order_header = ['Id','OrderAt','StoreId','UserId']
    orderitem_header = ['Id','OrderId','ItemId']

    def __init__(self, table_type:str, count:int):
        self.table_type = table_type
        if self.table_type == 'user':
            self.header = DisplayData.user_header
            self.data = UserGenerator().generate_user(count)
        elif self.table_type == 'store':
            self.header = DisplayData.store_header
            self.data = StoreGenerator().generate_store(count)
        elif self.table_type == 'item':
            self.header = DisplayData.item_header
            self.data = ItemGenerator().generate_item(count)
        elif self.table_type == 'order':
            self.header = DisplayData.order_header
            self.data = OrderGenerator().generate_order(count)
        elif self.table_type == 'orderitem':
            self.header = DisplayData.orderitem_header
            self.data = OrderItemGenerator().generate_orderitem(count)
        else:
            print('유효하지 않은 테이블 타입입니다.')

    def print_data(self):
        for rowdata in self.data:
            current_line = []
            for i in range(len(rowdata)):
                current_line.append(f'{self.header[i]}:{rowdata[i]}')
            print(current_line)
        print(f'{self.table_type} 데이터가 생성되었습니다. 상단의 콘솔 메시지를 확인해주세요.')
    
    def export_csv(self):
        with open(f'output/{self.table_type}.csv','w', newline='', encoding='UTF-8') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(self.header)
            csv_writer.writerows(self.data)
        print(f'{self.table_type} 데이터가 csv로 생성되었습니다. export 폴더를 확인해주세요.')