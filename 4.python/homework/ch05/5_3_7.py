import datetime as dt

user_input = list(map(int,input().rstrip().split()))
user_date = dt.date(user_input[0],user_input[1],user_input[2])

next_day = user_date + dt.timedelta(1)

print(user_date.strftime('%m/%d/%Y'))
print(next_day.strftime('%m/%d/%Y'))
