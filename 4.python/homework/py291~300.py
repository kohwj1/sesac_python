#291
txt_path1 = r'C:\\Users\\user\\OneDrive\\Desktop\\매수종목1.txt'
with open(txt_path1,'w',encoding='UTF-8') as f1:
    f1.write('005930'+'\n')
    f1.write('005380'+'\n')
    f1.write('035420')

#292
txt_path2 = r'C:\\Users\\user\\OneDrive\\Desktop\\매수종목2.txt'
with open(txt_path2,'w',encoding='UTF-8') as f2:
    f2.write('005930 삼성전자'+'\n')
    f2.write('005380 현대차'+'\n')
    f2.write('035420 NAVER')

#293
import csv
with open(r'C:\\Users\\user\\OneDrive\\Desktop\\매수종목1.csv', 'w', encoding='cp949') as my_csv:
    csv_write = csv.writer(my_csv)
    csv_write.writerow(['종목명', '종목코드', 'PER'])
    csv_write.writerow(['삼성전자', '005930', 15.79])
    csv_write.writerow(['NAVER', '035420', 55.82])

#294
my_stock1 = []
# txt_path1 = r'C:\\Users\\user\\OneDrive\\Desktop\\매수종목1.txt'
with open(txt_path1,'r',encoding='UTF-8') as f1:
    lines = f1.readlines()
    for line in lines:
        my_stock1.append(line.replace('\n',''))

#295
my_stock2 = {}
# txt_path2 = r'C:\\Users\\user\\OneDrive\\Desktop\\매수종목2.txt'
with open(txt_path2,'r',encoding='UTF-8') as f2:
    lines = f2.readlines()
    for line in lines:
        code, corp_name = line.split()
        my_stock2[code] = corp_name

#296
per = ["10.31", "", "8.00"]
for i in per:
    try:
        print(float(i))
    except ValueError:
        print(0)


#297
float_per = []
for num in per:
    try:
        float_per.append(float(num))
    except ValueError:
        float_per.append(0)

#298
try:
    print(123456 / 0)
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다')

#299
data = [1, 2, 3]
for i in range(5):
    try:
        print(data[i])
    except IndexError as err:
        print(err)

#300
per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(per))
    except TypeError:
        print('리스트 그 자체는 실수로 변환할 수 없습니다 리스트 내부의 내용물을 꺼내서 for 구문을 돌려야')
    finally:
        print('암튼 이 줄은 무조건 시랳ㅇ되어야 합니다.')
