import random

class ItemNameGenerator:
    def __init__(self, file_path):
        self.item_list = self.load_data_from_file(file_path)

    def load_data_from_file(self, file_path):
        with open(file_path,'r',encoding='UTF-8') as file:
            data = file.read().splitlines()
        return data

    def generate_itemname(self):
        return random.choice(self.item_list)
    
# if __name__ == '__main__':
#     test_instance = ItemNameGenerator(r'5.Project\1.data_gen\items.txt')
#     print(test_instance.generate_itemname())