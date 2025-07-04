from generators.common.getData import GetData

class ItemName(GetData):
    def generate(self) -> str:
        return self.get_rand('data/items.txt')
    
# if __name__ == '__main__':
#     test_instance = ItemNameGenerator(r'5.Project\1.data_gen\items.txt')
#     print(test_instance.generate_itemname())