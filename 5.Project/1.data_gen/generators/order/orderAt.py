# 임의의 연월일시분초 생성
from generators.common.date import Date
import random
    
class OrderedAt:
    def generate(self) -> str:
        day = Date().generate_date('order')
        self.hour = random.randint(0,23)
        self.minute = random.randint(0,59)
        self.second = random.randint(0,59)
        return f'{day} {self.hour:02d}:{self.minute:02d}:{self.second:02d}'