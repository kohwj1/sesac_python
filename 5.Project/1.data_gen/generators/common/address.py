from generators.common.getData import GetData
import random

class Address(GetData):
    def city(self) -> str:
        megacity = random.choice(['서울', '대전', '대구', '인천', '부산', '울산', '광주', '세종'])
        division = self.get_rand('data/divisions.txt')
        return f'{megacity} {division}'

    def generate(self) -> str:
        city = self.city()
        street_num = random.randint(1,20)
        post_num = random.randint(1,100)
        return f'{city}구 {street_num}길 {post_num}'