registry = {}

#사용자가 입력한 문자열과 클래스를 딕셔너리로 연결하기 위해 데코레이터를 사용..
def register(key):
    def decorator(cls):
        registry[key] = cls
        return cls
    return decorator

def get_class(key):
    return registry.get(key)

#main.py에서 타입 체크 시 사용할 용도의 함수
def tablelist():
    return list(registry.keys())