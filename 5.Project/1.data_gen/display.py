from registry import get_class
import csv
    
class DisplayData:
    def __init__(self, table_type:str, count:int):
        self.table_type = table_type
        self.data = get_class(self.table_type)().generate(count)
        self.header = self.data[1]

    def print_data(self):
        for rowdata in self.data[0]:
            current_line = []
            for i in range(len(rowdata)):
                current_line.append(f'{self.header[i]}:{rowdata[i]}')
            print(current_line)
        print(f'{self.table_type} 데이터가 생성되었습니다. 상단의 콘솔 메시지를 확인해주세요.')
    
    def export_csv(self):
        with open(f'output/{self.table_type}.csv','w', newline='', encoding='UTF-8') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(self.header)
            csv_writer.writerows(self.data[0])
        print(f'{self.table_type} 데이터가 csv로 생성되었습니다. output 폴더를 확인해주세요.')