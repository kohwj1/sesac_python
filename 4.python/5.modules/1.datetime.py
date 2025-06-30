# https://docs.python.org/ko/3.10/library/dt.html (빌트인 모듈)
# import 방식
# import datetime
# from datetime import *
import datetime as dt

#모듈명.변수명
#모듈명.클래스명.함수명()

print(dt.MINYEAR)
print(dt.MAXYEAR)

print(dt.datetime.now())
print(dt.datetime.now().strftime('%Y-%m-%d'))
print(dt.datetime.now().strftime('%H:%M:%S'))

my_time = dt.dt(2025,6,30,10,45,00) #Class 'dt'
print(type(my_time))
print(my_time)