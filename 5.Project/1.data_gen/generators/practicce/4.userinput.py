from generators.user_generate import UserGenerator
import sys

class DisplayData(UserGenerator):
    def print_data(self, count):
        data = self.generate_user(count)
        for user_id, name, birth, gender, address in data:
            print(f'ID:{user_id}', end=',')
            print(f'Name:{name}', end=',')
            print(f'Birthday:{birth}', end=',')
            print(f'Gender:{gender}', end=',')
            print(f'Address:{address}')
#최종 실행

print(sys.argv) #입력 인자
# sys.argv[0] #실행 파일명 자기자신
# sys.argv[1] #첫 번째 인자

if len(sys.argv) > 1:
    num_data = int(sys.argv[1])
else:
    num_data = int(input('원하는 데이터 개수를 입력하세요: '))

my_data = DisplayData()
my_data.print_data(num_data)