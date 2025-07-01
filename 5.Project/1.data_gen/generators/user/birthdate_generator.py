import random
import datetime
    
class BirthGenerator:
    def generate_birth(self):
        year = random.randint(1990,2010)
        month = random.randint(1,12)
        day = random.randint(1,28)
        return f'{year}-{month:02d}-{day:02d}'

    def generate_age(self):
        return 30