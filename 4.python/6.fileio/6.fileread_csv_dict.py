import csv

file_path = 'text.csv'
data = []

with open(file_path,'r') as file:
    csv_reader = csv.DictReader(file) #파일을 읽기 위한 포인터 가져오기
    for row in csv_reader:
        data.append(row)

print(data)