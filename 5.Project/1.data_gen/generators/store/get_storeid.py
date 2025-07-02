#목표: store.csv의 id 컬럼을 가져와 리스트에 담는다
import pandas

class GetStoreId:
    def get_storeid(self):
        file = pandas.read_csv(r'export_csv/store.csv')
        store_id = file['Id']
        return list(store_id)
    
# if __name__ == '__main__':
#     test_instance = GetStoreId()
#     print(test_instance.get_storeid(), sep='\n')