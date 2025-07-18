import pandas
import random

class GetData:
    def get_uuid(self, table_type:str) -> list:
        if table_type not in ['user', 'store', 'item', 'order']:
            print('추출할 수 없는 타입입니다.')
        else:
            try: 
                file = pandas.read_csv(f'output/{table_type}.csv')
                uuid_list = file['Id']
                return list(uuid_list)
            except FileNotFoundError:
                print('csv 파일이 없습니다. 해당 csv가 생성되어 있는지 확인해주세요.')
    
    def get_txt(self, file_path:str) -> list:
        try:
            with open(file_path,'r',encoding='UTF-8') as file:
                data = file.read().splitlines()
            return data
        except FileNotFoundError:
                print('txt 파일이 없습니다. 경로를 다시 확인해주세요.')
    
    def get_rand(self, file_path) -> str:
        return random.choice(self.get_txt(file_path))
    
if __name__ == '__main__':
    test_instance = GetData()
    print(test_instance.get_uuid('user'), sep='\n')