class User:
    pass

class Store:
    pass

class Item:
    pass

class DisplayData:
    def __init__(self, data):
        self.handler = {
            User: self.display_user,
            Store: self.display_store,
            Item: self.display_item
        }

        handler = self.handler.get(type(data), self.unsupported_type)
        handler(data)

    def display_user(self,data):
        print(f'사용자: {data}')

    def display_store(self,data):
        print(f'상점 정보: {data}')

    def display_item(self,data):
        print(f'아이템 정보: {data}')

    def unsupported_type(self,data):
        print(f'미지원 타입: {data}')

DisplayData(User())
DisplayData(Store())
DisplayData(Item())
DisplayData(list())