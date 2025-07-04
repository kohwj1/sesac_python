from display import DisplayData
import sys

#최종 실행
if __name__ == '__main__':
    print(len(sys.argv))

    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print('필수 인자가 누락되었습니다. python generator.py "종류" "건수" "출력옵션(생략가능)"으로 입력해주세요!')
    else:
        create_type = ['user', 'store', 'item', 'order', 'orderitem'] #맨 위로
        if sys.argv[1] not in create_type:
            print(f'{sys.argv[1]}는 생성 가능한 제너레이터 유형이 아닙니다.\n생성 가능 유형: {create_type}')
        else:
            try:
                count = int(sys.argv[2])
                csv_data = DisplayData(sys.argv[1], count)
                # csv_data.export_csv()
                # csv_data.print_data()
                if len(sys.argv) == 4 and sys.argv[3] == 'csv': #실행인자가 4개이고 csv라고 명시한 경우
                    csv_data.export_csv()
                elif len(sys.argv) == 3 or sys.argv[3] == 'console': #실행인자가 3개(마지막 생략)거나 console이라고 명시한 경우
                    csv_data.print_data()
                else:
                    print('출력 옵션을 정확하게 입력해주세요.') #둘다 옵션도 필요할지?
            except ValueError:
                print('생성 횟수를 숫자로 입력해주세요')