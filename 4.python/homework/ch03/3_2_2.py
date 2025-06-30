from datetime import datetime

def triple(x):
    return x * 3

print(triple(2))
print(triple('x'))

def korean_age(birth_year):
    return datetime.today().year - birth_year + 1