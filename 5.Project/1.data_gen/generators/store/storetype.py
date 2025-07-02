from generators.common.getData import GetData

class StoreTypeGenerator(GetData):
    def generate_storetype(self) -> str:
        return self.get_rand('static/store_type.txt')
    
# if __name__ == '__main__':
#     test_instance = StoreTypeGenerator()
#     print(test_instance.generate_storetype())