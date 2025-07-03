import random

class PriceGenerator:        
    def generate_price(self) -> int:
        return random.randrange(2500,7000,500)
    
# if __name__ == '__main__':
#     test_instance = PriceGenerator()
#     print(test_instance.generate_price())