import uuid

class UserIdGenerator:
    def __init__(self):
        pass

    def generate_userid(self):
        return uuid.uuid4()