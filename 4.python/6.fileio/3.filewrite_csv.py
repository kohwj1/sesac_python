# https://docs.python.org/3.10/library/csv.html
import csv

file_path = 'text.csv'

data = [
    ['name','age','city'],
    ['John',25,'Seoul'],
    ['Jane',30,'Busan'],
    ['Bob',25,'Jeju'],
]

print(data)

for line in data:
    print(line)

with open(file_path,'w', newline='') as file:
    csv_writer = csv.writer(file) #파일을 쓰기 위한 포인터 가져오기
    csv_writer.writerows(data)
    csv_writer.writerow(['Alice',40,'Suwon'])

print('CSV 쓰기 완료')