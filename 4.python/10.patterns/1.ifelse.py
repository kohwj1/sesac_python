class DisplayData:
    def __init__(self, data):
        if type(data) == 'str':
            self.display_str(data)
        elif type(data) == 'list':
            self.display_list(data)
        elif type(data) == 'dict':
            self.display_dict(data)
        else:
            raise TypeError('미지원 타입')
    
    def display_str(self,data):
        print(f'문자열: {data}')

    def display_list(self,data):
        print(f'리스트: {data}')

    def display_dict(self,data):
        print(f'딕셔너리: {data}')


DisplayData('hello')
DisplayData([1, 2, 3])
DisplayData({'data':1})