import random
import datetime
    
class DateGenerator:
    def __init__(self):
        self.year = 1990
        self.month = 1
        self.day = 1

    def generate_date(self, datetype:str) -> str:
        if datetype == 'birth':
            self.year = random.randint(1990,2010)
        else:
            self.year = random.randint(2020,2025)
        self.month = random.randint(1,12)
        self.day = random.randint(1,28)
        return f'{self.year}-{self.month:02d}-{self.day:02d}'

    def generate_age(self) -> int:
        today = datetime.datetime.now()
        age = today.year - self.year
        if (today.month < self.month) or (today.month == self.month and today.day < self.day):
            age -= 1

        return age