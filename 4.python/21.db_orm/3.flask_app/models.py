from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() #인스턴스 생성 시 instance 폴더에 DB 생성 

#사용자 모델 정의
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)

    #객체를 프린트로 출력할 때의 포맷을 정의하는 함수
    def __repr__(self):
        return f'<User {self.id}: {self.name}, {self.age}>'
    
    #string으로 캐스팅하는 함수
    def __str__(self):
        return f'문자열 <User {self.id}: {self.name}, {self.age}>'