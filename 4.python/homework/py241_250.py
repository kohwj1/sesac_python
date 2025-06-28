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
from datetime import datetime
import time
i = 0
while i < 10:
    print(datetime.now())
    time.sleep(1)
    i += 1

#247
# 전체 모듈 필요: import 모듈명
# 특정 함수만 사용: from 모듈명 import 함수명
# 간결한 호출 필요: import 모듈명 as 별칭
# 특별한 이유 없이 권장 안 함: from 모듈명 import *

#248
import os
print(os.getcwd())

#249
os.rename(r'C:\\Users\\user\\OneDrive\\Desktop\\파일명바꿀거.txt',r'C:\\Users\\user\\OneDrive\\Desktop\\파일명바꿀거222.txt')

#250
import numpy
for i in numpy.arange(0.0,5.1,0.1):
    print(round(i,1))