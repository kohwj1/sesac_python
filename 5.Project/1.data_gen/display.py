from generators.table.user import User
from generators.table.store import Store
from generators.table.item import Item
from generators.table.order import Order
from generators.table.orderitem import OrderItem
import csv

class DisplayData():
    header = {'user':['Id','Name','Gender','Age','Birthdate','Address'],
              'store':['Id','Name','Type','Address'],
              'item':['Id','Name','Type','UnitPrice'],
              'order':['Id','OrderAt','StoreId','UserId'],
              'orderitem': [['Id','OrderId','ItemId']]
              }
    instance = {'user':User(), 'store':Store(), 'item':Item(), 'order': Order(), 'orderitem':OrderItem()}

    def __init__(self, table_type:str, count:int):
        self.table_type = table_type
        self.header = DisplayData.header[self.table_type]
        self.data = DisplayData.instance[table_type].generate(count)

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
        print(f'{self.table_type} 데이터가 csv로 생성되었습니다. output 폴더를 확인해주세요.')