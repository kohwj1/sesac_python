# 임의의 연월일시분초 생성
import random
    
class OrderedAtGenerator:
    def generate_orderdate(self):
        self.year = random.randint(1990,2010)
        self.month = random.randint(1,12)
        self.day = random.randint(1,28)
        self.hour = random.randint(0,23)
        self.minute = random.randint(0,59)
        self.second = random.randint(0,59)
        return f'{self.year}-{self.month:02d}-{self.day:02d} {self.hour:02d}:{self.minute:02d}:{self.second:02d}'