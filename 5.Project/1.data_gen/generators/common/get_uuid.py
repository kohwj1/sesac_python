#목표: store.csv의 id 컬럼을 가져와 리스트에 담는다
import pandas

class GetUuid:
    def get_uuid(self, type):
        if type not in  ['user', 'store', 'item', 'order']:
            print('추출할 수 없는 타입입니다.')
        else:
            try: 
                file = pandas.read_csv(f'export/{type}.csv')
                uuid_list = file['Id']
                return list(uuid_list)
            except FileNotFoundError:
                # print('csv 파일이 없습니다. 해당 csv가 생성되어 있는지 확인해주세요.')
                pass
    
if __name__ == '__main__':
    test_instance = GetUuid()
    print(test_instance.get_uuid('user'), sep='\n')