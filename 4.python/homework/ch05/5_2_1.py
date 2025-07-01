#1
import calendar
print(dir(calendar))

#2
contain_leap = [item for item in dir(calendar) if 'leap' in item]
print(contain_leap)

#3
# help(calendar.isleap)

#4
print(calendar.isleap(2077))