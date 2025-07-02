# 임의의 연월일시분초 생성
from generators.common.date_generator import DateTimeGenerator
import random
    
class OrderedAtGenerator:
    def generate_orderdate(self):
        day = DateTimeGenerator().generate_date('order')
        self.hour = random.randint(0,23)
        self.minute = random.randint(0,59)
        self.second = random.randint(0,59)
        return f'{day} {self.hour:02d}:{self.minute:02d}:{self.second:02d}'