from app import app
from models import db, User

with app.app_context(): #app이 초기 실행되었을 때
    db.drop_all() #기존 DB 날리기
    db.create_all() #신규 생성

    db.session.add(User(name='Alice', age=30))
    db.session.add(User(name='Bob', age=25))
    db.session.add(User(name='Charlie', age=20))

    db.session.commit()

    for u in User.query.all():
        print (u)
        # print (u.id, u.name, u.age)

