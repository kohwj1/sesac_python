#목표: store.csv의 id 컬럼을 가져와 리스트에 담는다
import pandas

class GetUserId:
    def get_userid(self):
        file = pandas.read_csv(r'C:\Users\user\PycharmProjects\sesac_python\5.Project\1.data_gen\user.csv')
        user_id = file['Id']
        return list(user_id)
    
if __name__ == '__main__':
    test_instance = GetUserId()
    print(test_instance.get_userid(), sep='\n')