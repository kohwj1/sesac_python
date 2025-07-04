from generators.common.getData import GetData

class StoreType(GetData):
    def generate(self) -> str:
        return self.get_rand('data/store_type.txt')
    
# if __name__ == '__main__':
#     test_instance = StoreTypeGenerator()
#     print(test_instance.generate_storetype())