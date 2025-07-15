from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# engine = create_engine('mysql:///') #mysql을 사용한다면
engine = create_engine('sqlite:///example.db') #상대경로 설정 방식 --> instance라는 폴더를 생성함
# engine = create_engine('sqlite:////tmp/example.db') #절대경로 설정 방식
# engine = create_engine('sqlite:///./example.db') #절대경로 방식으로 현재 폴더 지정

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'  #테이블 이름을 직접 지정하고 싶을 때
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

#DB에게 테이블 생성 지시
Base.metadata.create_all(engine)

#세션을 통해 실제 DB에 CRUD를 함
Session = sessionmaker(bind=engine)
sess = Session() #sqlite3의 커서 역할?

new_user = User(name='Alice', age=30)
sess.add(new_user)  #SQL INSERT와 동일 역할
sess.commit()

users = sess.query(User).all()

for user in users:
    print(user.id, user.name, user.age)

# sess.close()


