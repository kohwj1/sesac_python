from generators.user.user_generator import UserGenerator
from generators.store.store_generator import StoreGenerator
from generators.store.item_generator import ItemGenerator
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
        with open('user.csv','w', newline='', encoding='UTF-8') as file:
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
        with open('store.csv','w', newline='', encoding='UTF-8') as file:
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
        with open('item.csv','w', newline='', encoding='UTF-8') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(['Id','Name','Type','UnitPrice'])
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
                    # item_data.print_data()
                    item_data.export_csv(count)
                elif gen_arg[1] == 'order':
                    pass
                elif gen_arg[1] == 'orderitem':
                    pass
            except ValueError:
                print('생성 횟수는 숫자로 입력해주세요')