import random

class Price:        
    def generate(self) -> int:
        return random.randrange(2500,6501,500)
    
# if __name__ == '__main__':
#     test_instance = PriceGenerator()
#     print(test_instance.generate_price())