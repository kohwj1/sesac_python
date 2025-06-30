import datetime

year, month, day = map(int, input().split())

print(f'{month:02}/{day:02}/{year}')

day += 1

if month == 2 and day > 28:
    month +=1
    day = 1

elif month == 12 and day > 31:
    year += 1
    month = 1
    day = 1
elif month in [1,3,5,7,8,10] and day > 31:
    month +=1
    day = 1
elif month in [4,6,9,11] and day > 30:
    month +=1
    day = 1
else:
    pass

print(f'{month:02}/{day:02}/{year}')