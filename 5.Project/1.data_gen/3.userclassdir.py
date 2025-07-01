from generators.user_generate import UserGenerator

class DisplayData(UserGenerator):
    def print_data(self, count):
        data = self.generate_user(count)
        for name, birth, gender, address in data:
            print(f'Name: {name}', end=', ')
            print(f'Birthday: {birth}', end=', ')
            print(f'Gender: {gender}', end=', ')
            print(f'Address: {address}')

num_data = int(input('원하는 데이터 갯수를 입력하세요: '))

my_data = DisplayData()
my_data.print_data(num_data)