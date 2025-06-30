# https://docs.python.org/3.10/library/csv.html
import csv

file_path = 'text.csv'

data = [
    {'name':'John','age':25,'city':'Seoul'},
    {'name':'Jane','age':30,'city':'Busan'},
    {'name':'Bob','age':35,'city':'Jeju'},
]

for person in data:
    # print(person)
    print(f'이름은 {person["name"]} 및 나이는 {person["age"]}')
    # for key, value in person.items():
        # print(f'key: {key}, value:{value}')

with open(file_path,'w', newline='') as file:
    # headers = ['name','age', 'city]
    headers = data[0].keys()
    csv_writer = csv.DictWriter(file, fieldnames=headers) #딕셔너리로 파일을 쓰기 위한 포인터 가져오기
    csv_writer.writeheader()
    csv_writer.writerows(data)

# print('CSV 쓰기 완료')