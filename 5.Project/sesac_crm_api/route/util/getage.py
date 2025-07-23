import datetime

def get_age(birthdate:datetime):
    today = datetime.date.today()
    birthday = birthdate.date()

    age = today.year - birthday.year

    if (birthday.month > today.month) or ((birthday.month == today.month) and (birthday.day > today.day)):
        age += -1
    
    return age