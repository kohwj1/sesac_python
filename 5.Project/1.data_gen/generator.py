from generators.table.user_generator import UserGenerator
from generators.table.store_generator import StoreGenerator
from generators.table.item_generator import ItemGenerator
from generators.table.order_generator import OrderGenerator
from generators.table.orderitem_generator import OrderItemGenerator
import sys, csv

class UserDisplayData(UserGenerator):
    def print_data(self, count):
        data = self.generate_user(count)
        for user_id, name, gender, age, birthday, address in data:
            print(f'ID:{user_id}', end=',')
            print(f'Name:{name}', end=',')
            print(f'Gender:{gender}', end=',')
            print(f'Age:{age}', end=',')
            print(f'Birthday:{birthday}', end=',')
            print(f'Address:{address}')
    def export_csv(self, count):
        data = self.generate_user(count)
        with open('export/user.csv','w', newline='', encoding='UTF-8') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(['Id','Name','Gender','Age','Birthdate','Address'])
            csv_writer.writerows(data)
        

class StoreDisplayData(StoreGenerator):
    def print_data(self, count):
        data = self.generate_store(count)
        for store_id, store_name, store_type, store_address in data:
            print(f'ID:{store_id}', end=',')
            print(f'Name:{store_name}', end=',')
            print(f'Type:{store_type}', end=',')
            print(f'Address:{store_address}')
    def export_csv(self, count):
        data = self.generate_store(count)
        with open('export/store.csv','w', newline='', encoding='UTF-8') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(['Id','Name','Type','Address'])
            csv_writer.writerows(data)

class ItemDisplayData(ItemGenerator):
    def print_data(self, count):
        data = self.generate_item(count)
        for item_id, item_name, item_type, item_price in data:
            print(f'ID:{item_id}', end=',')
            print(f'Name:{item_name}', end=',')
            print(f'Type:{item_type}', end=',')
            print(f'UnitPrice:{item_price}')
    def export_csv(self, count):
        data = self.generate_item(count)
        with open('export/item.csv','w', newline='', encoding='UTF-8') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(['Id','Name','Type','UnitPrice'])
            csv_writer.writerows(data)

class OrderDisplayData(OrderGenerator):
    def print_data(self, count):
        data = self.generate_order(count)
        for order_id, order_at, store_id, user_id in data:
            print(f'ID:{order_id}', end=',')
            print(f'OrderAt:{order_at}', end=',')
            print(f'StoreId:{store_id}', end=',')
            print(f'UserId:{user_id}')
    def export_csv(self, count):
        data = self.generate_order(count)
        with open('export/order.csv','w', newline='', encoding='UTF-8') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(['Id','OrderAt','StoreId','UserId'])
            csv_writer.writerows(data)
            
class OrderItemDisplayData(OrderItemGenerator):
    def print_data(self, count):
        data = self.generate_orderitem(count)
        for orderitem_id, order_id, item_id in data:
            print(f'ID:{orderitem_id}', end=',')
            print(f'OrderId:{order_id}', end=',')
            print(f'ItemId:{item_id}')
    def export_csv(self, count):
        data = self.generate_orderitem(count)
        with open('export/orderitem.csv','w', newline='', encoding='UTF-8') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(['Id','OrderId','ItemId'])
            csv_writer.writerows(data)

#최종 실행
if __name__ == '__main__':
    gen_arg = sys.argv

    if len(gen_arg) != 3:
        print('필수 인자 누락')
    else:
        if gen_arg[1] not in ['user', 'store', 'item', 'order', 'orderitem']:
            print('생성 가능한 제너레이터 유형이 아닙니다')
        else:
            try:
                count = int(gen_arg[2])
                if gen_arg[1] == 'user':
                    user_data = UserDisplayData()
                    # user_data.print_data(count)
                    user_data.export_csv(count)
                elif gen_arg[1] == 'store':
                    store_data = StoreDisplayData()
                    # store_data.print_data(count)
                    store_data.export_csv(count)
                elif gen_arg[1] == 'item':
                    item_data = ItemDisplayData()
                    # item_data.print_data(count)
                    item_data.export_csv(count)
                elif gen_arg[1] == 'order':
                    order_data = OrderDisplayData()
                    # order_data.print_data(count)
                    order_data.export_csv(count)
                elif gen_arg[1] == 'orderitem':
                    orderitem_data = OrderItemDisplayData()
                    # orderitem_data.print_data(count)
                    orderitem_data.export_csv(count)
            except ValueError:
                print('생성 횟수는 숫자로 입력해주세요')