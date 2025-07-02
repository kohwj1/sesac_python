from display import DisplayData
import sys

#최종 실행
if __name__ == '__main__':
    gen_arg = sys.argv

    if len(gen_arg) != 3:
        print('필수 인자가 누락되었습니다. python generator.py "테이블종류" "건수"로 입력해주세요!')
    else:
        create_type = ['user', 'store', 'item', 'order', 'orderitem']
        if gen_arg[1] not in create_type:
            print(f'{gen_arg[1]}는 생성 가능한 제너레이터 유형이 아닙니다.\n생성 가능 유형: {create_type}')
        else:
            try:
                count = int(gen_arg[2])
                csv_data = DisplayData(gen_arg[1], count)
                csv_data.print_data()
                csv_data.export_csv()
            except ValueError:
                print('생성 횟수를 숫자로 입력해주세요')