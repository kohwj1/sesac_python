#241
from datetime import datetime
print(datetime.now())

#242
print(type(datetime.now()))

#243
from datetime import timedelta
print(datetime.now() - timedelta(days=5))
print(datetime.now() - timedelta(days=4))
print(datetime.now() - timedelta(days=3))
print(datetime.now() - timedelta(days=2))
print(datetime.now() - timedelta(days=1))

#244
print(datetime.strftime(datetime.now(),'%H:%M:%S'))

#245
print(datetime.strptime('2020-05-04','%Y-%m-%d'))

#246
# import time
# while True:
#     print(datetime.now())
#     time.sleep(1)

#247
#추가 공부 필요

#248
import os
print(os.getcwd())

#249
# os.rename('옛날경로파일명','변경할경로파일명')

#250
import numpy
for i in numpy.arange(0.0,5.1,0.1):
    print(round(i,1))