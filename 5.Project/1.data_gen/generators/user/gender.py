import random

class GenderGenerator:
    def generate_gender(self) -> str:
        return random.choice(['Male','Female'])